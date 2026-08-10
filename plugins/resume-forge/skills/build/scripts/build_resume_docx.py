#!/usr/bin/env python3
"""Build a house-style resume .docx from a JSON spec, then base64 it for Drive.

Why a .docx and not HTML: Google Docs' HTML importer silently drops page margins
and has no way at all to express a right tab stop, so the two things the house
style depends on most cannot survive that route. A .docx carries both natively
and Google preserves them on import. Verified by round-tripping a built document
back out of Drive: margins came back at 720 twips (0.5") and all right tab stops
at exactly 7.50".

Standard library only. No third-party packages, no network, no shell commands,
no platform-specific paths. Runs the same on macOS, Windows and Linux.

Usage
-----
    python3 build_resume_docx.py spec.json out.docx          # write the .docx
    python3 build_resume_docx.py spec.json out.docx --base64 # also print base64
    python3 build_resume_docx.py --verify built.b64 pasted.b64

Pass the printed base64 to the Drive connector as `base64Content` with
contentMimeType
`application/vnd.openxmlformats-officedocument.wordprocessingml.document`.
Drive converts it to a Google Doc automatically.

Verify before uploading. An agent composing the connector call has to reproduce
the payload as literal text, and that transcription step has corrupted single
characters in practice even at 4KB. Save the payload you are about to send to a
file, run `--verify` against the built payload, and only upload once it prints
IDENTICAL. On a mismatch it lists every differing position with the correct and
the corrupted context side by side, so each error can be patched directly.
Whitespace and line breaks are ignored; only the base64 characters count.

Spec format: see spec.example.json next to this file.
"""

import base64
import json
import sys
import zipfile
from xml.sax.saxutils import escape

WNS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
TWIP = 1440

# House style. Changing these means changing references/house-style.md too.
MARGIN = int(0.50 * TWIP)        # 720  - all four sides
TAB_RIGHT = int(7.50 * TWIP)     # 10800 - the ruler runs 0.00" to 7.50"
BULLET_IND = (403, 259)          # text at 0.28", glyph at 0.10"
GAP_JOB, GAP_TITLE, GAP_SECTION = 1, 3, 7   # the only three gap sizes
GAPS_ALLOWED = (1, 3, 5, 7)      # 5 is a permitted tighter section gap


def run(text="", *, sz=11, bold=False, underline=False, tab=False):
    rpr = ['<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>']
    if bold:
        rpr.append("<w:b/>")
    if underline:
        rpr.append('<w:u w:val="single"/>')
    rpr.append(f'<w:sz w:val="{int(sz * 2)}"/><w:szCs w:val="{int(sz * 2)}"/>')
    body = "<w:tab/>" if tab else ""
    if text:
        body += f'<w:t xml:space="preserve">{escape(text)}</w:t>'
    return f'<w:r><w:rPr>{"".join(rpr)}</w:rPr>{body}</w:r>'


def para(runs, *, align=None, tabstop=False, ind=None, sz=11):
    p = ["<w:pPr>"]
    if tabstop:
        p.append(f'<w:tabs><w:tab w:val="right" w:pos="{TAB_RIGHT}"/></w:tabs>')
    if ind:
        p.append(f'<w:ind w:left="{ind[0]}" w:hanging="{ind[1]}"/>')
    p.append('<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>')
    if align:
        p.append(f'<w:jc w:val="{align}"/>')
    p.append('<w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/>'
             f'<w:sz w:val="{int(sz * 2)}"/></w:rPr>')
    p.append("</w:pPr>")
    return f'<w:p>{"".join(p)}{"".join(runs)}</w:p>'


def gap(pt):
    """The gap IS an empty paragraph at this font size, never paragraph spacing.

    Only 1, 3, 5 or 7 point. The guard exists because inventing a fourth value
    is how a document stops being internally consistent."""
    if pt not in GAPS_ALLOWED:
        raise ValueError(f"gap must be one of {GAPS_ALLOWED} point, got {pt}")
    return para([], sz=pt)


def section(name):
    return para([run(name, bold=True, underline=True)])


def dated(left, date, issuer=None):
    """Role, institution or certification line. Left text AND date both bold,
    date flush right on the 7.50" stop.

    `issuer` is the certifying body, set in regular weight after the bold name.
    Bold marks the entity that owns the date; the issuer describes it, the same
    way a degree line describes an institution. Bolding it too turns a long
    certifications block into a slab of bold with no contrast left to spend."""
    runs = [run(left, bold=True)]
    if issuer:
        runs.append(run(", " + issuer))
    if date:
        runs.append(run(date, bold=True, tab=True))
    return para(runs, tabstop=True)


def bullet(text):
    return para([run("•   " + text)], ind=BULLET_IND)


def build_paragraphs(spec):
    P = []
    c = spec["contact"]
    P.append(para([run(c["name"], sz=20, bold=True)], align="center", sz=20))
    P.append(para([run(c["location"])], align="center"))
    P.append(para([run("  |  ".join(c["links"]))], align="center"))
    P.append(gap(GAP_TITLE))
    P.append(para([run(spec["target_title"], sz=16, bold=True)],
                  align="center", sz=16))
    P.append(gap(GAP_TITLE))
    # The summary is the one centred body block - it belongs to the header group.
    P.append(para([run(spec["summary"])], align="center"))

    for sec in spec["sections"]:
        P.append(gap(GAP_SECTION))
        P.append(section(sec["header"]))
        kind = sec.get("kind", "entries")
        # "grouped" renders like skills: a bold label and regular items. It is
        # what a certifications block collapses to once it is too long to list
        # one per line. Same rendering, different name, so the spec reads as
        # what it is rather than borrowing the skills label.
        if kind in ("skills", "grouped"):
            for label, items in sec["items"]:
                P.append(para([run(label, bold=True), run(" " + items)]))
            continue
        for i, entry in enumerate(sec["entries"]):
            if i:
                P.append(gap(GAP_JOB))
            P.append(dated(entry["left"], entry.get("date", ""),
                           entry.get("issuer")))
            for line in entry.get("lines", []):
                P.append(para([run(line)]))
            for b in entry.get("bullets", []):
                P.append(bullet(b))
    return P


def write_docx(paragraphs, path):
    doc = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
           f'<w:document {WNS}><w:body>{"".join(paragraphs)}'
           '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
           f'<w:pgMar w:top="{MARGIN}" w:right="{MARGIN}" w:bottom="{MARGIN}" '
           f'w:left="{MARGIN}" w:header="720" w:footer="720" w:gutter="0"/>'
           '</w:sectPr></w:body></w:document>')
    types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
             '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
             '<Default Extension="xml" ContentType="application/xml"/>'
             '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
             '</Types>')
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
            '</Relationships>')
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/document.xml", doc)


def verify(built_path, pasted_path):
    """Compare two base64 payload files, ignoring whitespace. Exit 0 only if
    the base64 characters match exactly; otherwise report every mismatch with
    enough surrounding context to patch the pasted copy."""
    def load(path):
        with open(path, encoding="utf-8") as fh:
            return "".join(fh.read().split())
    built, pasted = load(built_path), load(pasted_path)
    if built == pasted:
        print(f"IDENTICAL ({len(built)} base64 chars)")
        return 0
    if len(built) != len(pasted):
        print(f"LENGTH MISMATCH: built {len(built)} chars, "
              f"pasted {len(pasted)} chars")
    diffs = [i for i, (a, b) in enumerate(zip(built, pasted)) if a != b]
    for i in diffs[:20]:
        lo, hi = max(0, i - 15), i + 16
        print(f"char {i}: built '{built[i]}' vs pasted '{pasted[i]}'")
        print(f"  built:  ...{built[lo:hi]}...")
        print(f"  pasted: ...{pasted[lo:hi]}...")
    if len(diffs) > 20:
        print(f"...and {len(diffs) - 20} more differing positions")
    print("DO NOT UPLOAD. Patch the pasted copy and verify again.")
    return 1


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    if sys.argv[1] == "--verify":
        if len(sys.argv) < 4:
            sys.exit(__doc__)
        sys.exit(verify(sys.argv[2], sys.argv[3]))
    with open(sys.argv[1], encoding="utf-8") as fh:
        spec = json.load(fh)
    out = sys.argv[2]
    write_docx(build_paragraphs(spec), out)
    with open(out, "rb") as fh:
        blob = fh.read()
    print(f"wrote {out} ({len(blob)} bytes)", file=sys.stderr)
    if "--base64" in sys.argv:
        print(base64.b64encode(blob).decode())


if __name__ == "__main__":
    main()
