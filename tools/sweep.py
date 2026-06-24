#!/usr/bin/env python3
"""The Keep — nightly structural sweep. Pure stdlib, no network, no LLM, no secrets.

Three jobs, all mechanical:
  1. Rebuild the AUTO-INDEX managed block in every index.md — a progressive-disclosure
     TOC of that directory's concepts + sub-sections. Only the block is touched; curated
     prose around it is preserved. Idempotent (invariant #11).
  2. Link-check absolute bundle-relative links — WARN only. A link to an unwritten page
     is a TODO, not an error (invariant #12).
  3. Dedup-flag near-duplicate titles/descriptions — WARN only. Never auto-merges; the
     Librarian decides (with a human while the corpus is young).

The sweep never deletes and never fails the build — flagging is its whole job. The gate
(tools/checks.py) is what fails red. Writes are LF-only to keep the OKF frontmatter
regex happy on the Linux runner.
"""
import re
import difflib
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

START = "<!-- AUTO-INDEX:START (managed by nightly-sweep.yml — edits inside are overwritten) -->"
END = "<!-- AUTO-INDEX:END -->"

# Never listed as a concept in any TOC (containers, redirects, the contract).
EXCLUDE = {"index.md", "README.md", "AGENTS.md", "CLAUDE.md", "DEED.md"}
# Directories the sweep does not enter or index.
SKIP_DIRS = {".git", "_raw", "attic", "tools", ".github"}

FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
BLOCK_RE = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)


def parse_fm(text):
    m = FM_RE.match(text)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm


def _skipped(p):
    return any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)


def abs_link(p):
    return "/" + p.relative_to(ROOT).as_posix()


def entry_for(md):
    fm = parse_fm(md.read_text(encoding="utf-8", errors="replace"))
    title = fm.get("title") or md.stem
    desc = fm.get("description", "")
    return f"- [{title}]({abs_link(md)})" + (f" — {desc}" if desc else "")


def section_for(subdir):
    idx = subdir / "index.md"
    fm = parse_fm(idx.read_text(encoding="utf-8", errors="replace"))
    title = fm.get("title") or subdir.name
    desc = fm.get("description", "")
    return f"- [{title}]({abs_link(idx)})" + (f" — {desc}" if desc else "")


def build_block(d):
    concepts = sorted(
        (p for p in d.glob("*.md") if p.name not in EXCLUDE),
        key=lambda p: p.name,
    )
    subs = sorted(
        (s for s in d.iterdir()
         if s.is_dir() and s.name not in SKIP_DIRS and (s / "index.md").exists()),
        key=lambda s: s.name,
    )
    lines = [START]
    if concepts:
        lines.append("")
        lines.extend(entry_for(p) for p in concepts)
    if subs:
        lines.append("")
        lines.append("**Sections**")
        lines.extend(section_for(s) for s in subs)
    if not concepts and not subs:
        lines.append("")
        lines.append("_No concepts yet._")
    lines.append("")
    lines.append(END)
    return "\n".join(lines)


def index_dirs():
    yield ROOT
    for p in sorted(ROOT.rglob("*")):
        if p.is_dir() and not _skipped(p) and (p / "index.md").exists():
            yield p


def rebuild_indexes():
    changed = []
    for d in index_dirs():
        idx = d / "index.md"
        text = idx.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
        block = build_block(d)
        if START in text and END in text:
            new = BLOCK_RE.sub(lambda _m: block, text)
        else:
            new = text.rstrip() + "\n\n" + block + "\n"
        if new != text:
            idx.write_text(new, encoding="utf-8", newline="\n")
            changed.append(idx.relative_to(ROOT).as_posix())
    return changed


def all_live_md():
    for p in ROOT.rglob("*.md"):
        if not _skipped(p):
            yield p


LINK_RE = re.compile(r"\[[^\]]*\]\((/[^)\s#]+)(?:#[^)]*)?\)")


def link_check():
    missing = []
    for p in all_live_md():
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in LINK_RE.finditer(text):
            target = (ROOT / m.group(1).lstrip("/"))
            if not target.exists():
                missing.append((p.relative_to(ROOT).as_posix(), m.group(1)))
    return missing


def dedup_flag():
    items = []
    for p in all_live_md():
        if p.name in EXCLUDE:
            continue
        fm = parse_fm(p.read_text(encoding="utf-8", errors="replace"))
        items.append((
            p.relative_to(ROOT).as_posix(),
            (fm.get("title") or "").lower().strip(),
            (fm.get("description") or "").lower().strip(),
        ))
    flags = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            pi, ti, di = items[i]
            pj, tj, dj = items[j]
            if ti and ti == tj:
                flags.append(f"identical title '{ti}': {pi} <-> {pj}")
            elif ti and tj and difflib.SequenceMatcher(None, ti, tj).ratio() > 0.90:
                flags.append(f"near-duplicate title: {pi} <-> {pj}")
            if di and dj and difflib.SequenceMatcher(None, di, dj).ratio() > 0.92:
                flags.append(f"near-duplicate description: {pi} <-> {pj}")
    return flags


def main():
    changed = rebuild_indexes()
    if changed:
        print("Rebuilt index TOCs:")
        for c in changed:
            print("  -", c)
    else:
        print("Indexes already current — no changes.")

    for src, target in link_check():
        print(f"::warning file={src}::link to missing path '{target}' (unwritten page = TODO, not an error)")

    for f in dedup_flag():
        print(f"::warning::dedup — {f}")

    print("Sweep complete (flag-only; the gate is tools/checks.py).")


if __name__ == "__main__":
    main()
