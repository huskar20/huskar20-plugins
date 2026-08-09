#!/usr/bin/env python3
"""Check the hyperlinks inside a .docx against what their display text claims.

Covers the two link items on the review checklist that cannot be verified by
reading the rendered page:

- A hyperlink whose display text says one address while the underlying target
  points somewhere else (usually a stale copy-paste). Invisible on paper, and
  the reader who clicks it lands on the wrong profile.
- Text that looks like a URL or email but carries no hyperlink at all, so the
  exported PDF renders it as dead text.

Also reports display text that still carries a scheme prefix (https://www.),
which the house style prints in display form instead.

Standard library only. Usage:

    python3 check_links.py <resume.docx>

Prints one line per finding plus a summary. Exit code 0 when clean, 1 when
there are findings, 2 on unusable input.
"""

import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
PR = "{http://schemas.openxmlformats.org/package/2006/relationships}"

URL_LIKE = re.compile(
    r"(?:https?://)?(?:www\.)?[a-z0-9][a-z0-9-]*(?:\.[a-z0-9-]+)+(?:/[^\s|•·]*)?",
    re.IGNORECASE)
EMAIL = re.compile(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", re.IGNORECASE)


def normalize(url):
    """Reduce a URL to host+path so display text and target can be compared."""
    url = url.strip().rstrip("/.,;")
    url = re.sub(r"^(mailto:|https?://)", "", url, flags=re.IGNORECASE)
    url = re.sub(r"^www\.", "", url, flags=re.IGNORECASE)
    return url.lower()


def main(path):
    try:
        zf = zipfile.ZipFile(path)
        rels_xml = zf.read("word/_rels/document.xml.rels")
        doc_xml = zf.read("word/document.xml")
    except (OSError, zipfile.BadZipFile, KeyError) as exc:
        print(f"cannot read {path}: {exc}")
        return 2

    targets = {
        rel.get("Id"): rel.get("Target")
        for rel in ET.fromstring(rels_xml)
        if rel.tag == f"{PR}Relationship"
        and rel.get("Type", "").endswith("/hyperlink")
    }

    findings = []
    hyperlinked_texts = []
    root = ET.fromstring(doc_xml)

    for link in root.iter(f"{W}hyperlink"):
        rid = link.get(f"{R}id")
        if rid is None:          # internal bookmark anchor, not a URL
            continue
        display = "".join(t.text or "" for t in link.iter(f"{W}t")).strip()
        target = targets.get(rid, "")
        hyperlinked_texts.append(display)

        if not target:
            findings.append(f"NO TARGET      '{display}' is a hyperlink with no target URL")
            continue
        if re.match(r"^https?://www\.", display, re.IGNORECASE):
            findings.append(f"DISPLAY FORM   '{display}' — print it without the https://www. prefix")
        if URL_LIKE.fullmatch(display) or EMAIL.fullmatch(display):
            if normalize(display) != normalize(target):
                findings.append(
                    f"MISMATCH       text says '{display}' but the link goes to '{target}'")
        elif " " in target or not re.match(r"^(https?://|mailto:)", target, re.IGNORECASE):
            findings.append(f"MALFORMED      '{display}' points at '{target}'")

    # URL-looking plain text that carries no hyperlink at all
    linked = " ".join(hyperlinked_texts)
    for para in root.iter(f"{W}p"):
        if any(True for _ in para.iter(f"{W}hyperlink")):
            continue
        text = "".join(t.text or "" for t in para.iter(f"{W}t"))
        for match in list(URL_LIKE.finditer(text)) + list(EMAIL.finditer(text)):
            frag = match.group().rstrip("/.,;")
            if "@" not in frag and "/" not in frag and frag.count(".") < 2 and \
                    not re.match(r"^(www\.|https?)", frag, re.IGNORECASE):
                continue     # plain words like 'Node.js' — not a URL claim
            if frag not in linked:
                findings.append(f"NOT HYPERLINKED  '{frag}' is plain text; the exported PDF gets no link")

    for line in findings:
        print(line)
    print(f"\n{len(findings)} link finding(s) in {path}")
    return 1 if findings else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
