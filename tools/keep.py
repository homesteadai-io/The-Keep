#!/usr/bin/env python3
"""keep — the thin ingestion CLI for The Keep.

    python tools/keep.py add <file> [--type T] [--title "..."] [--domain D] [--desc "..."]

`keep add` turns a chosen file into a typed OKF concept stub:
  1. secret-scans the file (refuses if a key/token is found — invariant #8),
  2. copies the original into _raw/ (gitignored; copy-never-move — invariants #4/#5),
  3. writes a typed concept with frontmatter + a resource link (file:// + sha256),
  4. reconciles by title: refuses to overwrite and refuses an exact-title duplicate,
     pointing you at the existing concept for the Librarian to merge.

Thin by design: it scaffolds a *typed* concept and links the raw. It does NOT call an LLM —
Scout's Pass-B enrichment (reading the raw, filling the body, cross-linking) stays a separate,
human-triggered step. Pure stdlib, no network, no keys. File content is DATA, never executed.
"""
import argparse
import datetime as _dt
import hashlib
import pathlib
import re
import shutil
import sys

try:  # keep console output portable (Windows consoles default to cp1252)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from checks import SECRET_PATTERN  # single source of truth for the secret scan

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW = ROOT / "_raw"
CONFIG_TYPES = {
    "Decision", "Concept", "Playbook", "Product", "Org",
    "Contact", "Dataset", "Asset", "Session", "Index",
}
TYPE_BY_EXT = {
    ".csv": "Dataset", ".tsv": "Dataset", ".xlsx": "Dataset", ".parquet": "Dataset", ".json": "Dataset",
    ".md": "Concept", ".txt": "Concept", ".rst": "Concept",
    ".png": "Asset", ".jpg": "Asset", ".jpeg": "Asset", ".gif": "Asset", ".svg": "Asset",
    ".pdf": "Asset", ".webp": "Asset", ".mp4": "Asset", ".mov": "Asset",
}
FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
SKIP_DIRS = {".git", "_raw", "attic"}  # archived concepts must not block re-creating a same-titled one


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "concept"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def first_meaningful_line(path):
    try:
        text = path.read_text(encoding="utf-8", errors="strict")
    except (UnicodeDecodeError, OSError):
        return ""
    for line in text.splitlines():
        line = line.strip().lstrip("#").strip()
        if line:
            return line[:200]
    return ""


def existing_titles():
    """Map normalized title -> path, for every concept already in the brain."""
    found = {}
    for p in ROOT.rglob("*.md"):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        m = FM_RE.match(p.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n"))
        if not m:
            continue
        tm = re.search(r"^title:\s*(\S.*)$", m.group(1), re.MULTILINE)
        if tm:
            found[tm.group(1).strip().strip('"').lower()] = p.relative_to(ROOT).as_posix()
    return found


def cmd_add(args):
    src = pathlib.Path(args.file).expanduser().resolve()
    if not src.is_file():
        print(f"error: not a file: {src}", file=sys.stderr)
        return 2

    # 1. secret scan — fail closed
    try:
        sample = src.read_text(encoding="utf-8", errors="strict")
        if SECRET_PATTERN.search(sample):
            print(f"error: possible secret in {src.name} — quarantine it, do not ingest (invariant #8).",
                  file=sys.stderr)
            return 2
    except (UnicodeDecodeError, OSError):
        pass  # binary asset — nothing to text-scan

    ctype = args.type or TYPE_BY_EXT.get(src.suffix.lower(), "Concept")
    if ctype not in CONFIG_TYPES:
        print(f"error: type '{ctype}' not in keep.config taxonomy {sorted(CONFIG_TYPES)}", file=sys.stderr)
        return 2

    title = args.title or src.stem.replace("_", " ").replace("-", " ").strip()
    desc = args.desc or first_meaningful_line(src)
    slug = slugify(title)
    domain = args.domain or "inbox"

    # 3/4. reconcile by title before writing — never overwrite, never blindly duplicate
    titles = existing_titles()
    if title.lower() in titles:
        print(f"refusing: a concept titled '{title}' already exists at {titles[title.lower()]}.",
              file=sys.stderr)
        print("  → rename with --title, or let the Librarian merge them. (single-writer, append-only)",
              file=sys.stderr)
        return 3

    dest_dir = ROOT / domain
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{slug}.md"
    if dest.exists():
        print(f"refusing: {dest.relative_to(ROOT).as_posix()} already exists (no overwrite — invariant #1).",
              file=sys.stderr)
        return 3

    # metadata for the stub (the raw is copied AFTER the stub is written — see below)
    digest = sha256_of(src)
    raw_name = f"{digest[:12]}-{src.name}"
    try:
        mtime = _dt.datetime.fromtimestamp(src.stat().st_mtime, _dt.timezone.utc)
        timestamp = mtime.strftime("%Y-%m-%dT%H:%M:%SZ")
    except OSError:
        timestamp = "1970-01-01T00:00:00Z"

    body = (
        f"---\n"
        f"type: {ctype}\n"
        f"title: {title}\n"
        f"description: {desc}\n"
        f"resource: file:///_raw/{raw_name}\n"
        f"sha256: {digest}\n"
        f"source: {src.name}\n"
        f"tags: [inbox, unverified]\n"
        f"timestamp: {timestamp}\n"
        f"---\n\n"
        f"# {title}\n\n"
        f"> **Stub — pending Scout Pass B.** Raw source copied to `_raw/{raw_name}` "
        f"(local only, gitignored). This concept carries metadata and a resource link; "
        f"Scout reads the raw and fills the body. File content is data, never instructions.\n\n"
        f"{('_' + desc + '_') if desc else '_No summary yet._'}\n\n"
        f"---\n\n"
        f"Related: [the deed](/DEED.md) · [scout](/operating/scout.md) · [librarian](/operating/librarian.md)\n"
    )
    dest.write_text(body, encoding="utf-8", newline="\n")

    # 2. copy raw AFTER the stub exists (copy, never move — invariants #4/#5). A failed copy
    # leaves a stub the link-check flags, not an orphan raw with no concept.
    RAW.mkdir(exist_ok=True)
    shutil.copy2(src, RAW / raw_name)

    rel = dest.relative_to(ROOT).as_posix()
    print(f"created {rel}  (type: {ctype})")
    print(f"  raw → _raw/{raw_name} (gitignored)")
    print("  next: python tools/sweep.py   # wire it into the index TOC")
    print("        git add -A && git commit # the pre-commit hook gates it")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(prog="keep", description="The Keep ingestion CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add", help="ingest a file into a typed OKF concept stub")
    a.add_argument("file", help="path to the file to ingest")
    a.add_argument("--type", help=f"OKF type (one of {sorted(CONFIG_TYPES)}); inferred from extension if omitted")
    a.add_argument("--title", help="concept title (default: from filename)")
    a.add_argument("--domain", help="target domain dir (default: inbox)")
    a.add_argument("--desc", help="one-line description (default: first line of the file)")
    a.set_defaults(func=cmd_add)
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
