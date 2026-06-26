#!/usr/bin/env python3
"""The Keep local tools.

V1 intentionally stays boring: stdlib only, plain Markdown, no daemon.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOMAINS = {
    "creative-coatings",
    "frostbite",
    "homesteadai-io",
    "ai-theory-builds",
    "keryke",
    "lyhna",
    "personal",
}
SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"xox[baprs]-[0-9A-Za-z-]+"),
    re.compile(r"ghp_[A-Za-z0-9]{36}"),
]


class KeepError(RuntimeError):
    pass


def rel(path: Path) -> str:
    return "/" + path.resolve().relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def secret_scan_text(text: str, label: str) -> None:
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            raise KeepError(f"secret scan failed for {label}: {pattern.pattern}")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "untitled"


def first_heading(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            title = stripped.lstrip("#").strip()
            if title:
                return title
    return fallback


def first_body_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("---") or stripped.startswith("#"):
            continue
        if ":" in stripped and len(stripped) < 80:
            continue
        return stripped[:180]
    return "Captured source for Librarian review."


def tokens(value: str) -> set[str]:
    return {part for part in re.split(r"[^a-z0-9]+", value.lower()) if len(part) > 2}


def infer_domain(path: Path, text: str) -> str:
    haystack = f"{path.name}\n{text[:4000]}".lower()
    hints = [
        ("lyhna", ["lyhna", "witness", "bind"]),
        ("keryke", ["keryke", "arlo", "talaria", "small-business ai", "small business ai", "crimson desert", "room spine"]),
        ("creative-coatings", ["creative coatings", "coatings", "paint", "masking"]),
        ("frostbite", ["frostbite", "feeders", "reptile"]),
        ("homesteadai-io", ["homestead", "the keep", "keeper", "scout", "librarian"]),
        ("ai-theory-builds", ["ai theory", "bengio", "lecun", "hopfield", "pearl", "hassabis"]),
        ("personal", ["adam", "personal"]),
    ]
    for domain, needles in hints:
        if any(needle in haystack for needle in needles):
            return domain
    return "personal"


def infer_type(text: str) -> str:
    lower = text[:3000].lower()
    if "decision" in lower or "decided" in lower:
        return "Decision"
    if "playbook" in lower or "workflow" in lower or "process" in lower:
        return "Playbook"
    if "product" in lower or "offering" in lower:
        return "Product"
    return "Concept"


def unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    for i in range(2, 100):
        candidate = path.with_name(f"{stem}-{i}{suffix}")
        if not candidate.exists():
            return candidate
    raise KeepError(f"could not find unique path for {path}")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = read_text(path)
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data, body


def write_log(message: str) -> Path:
    now = dt.datetime.now(dt.timezone.utc)
    path = ROOT / "write-logs" / f"{now:%Y-%m}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(
            f"""---
type: Session
title: Write log - {now:%B %Y}
description: Append-only Keeper write log for {now:%B %Y}.
tags: [homestead, keep, write-log]
timestamp: {now:%Y-%m-%dT00:00:00Z}
---

# Write Log - {now:%B %Y}
""",
            encoding="utf-8",
        )
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"\n- {now:%Y-%m-%dT%H:%M:%SZ} - {message}\n")
    return path


def domain_paths() -> list[Path]:
    return [ROOT / domain for domain in sorted(DOMAINS)]


def concept_files(domain_path: Path) -> list[Path]:
    if not domain_path.exists():
        return []
    return sorted(
        path
        for path in domain_path.glob("*.md")
        if path.name != "index.md" and path.is_file()
    )


def index_entry(path: Path) -> str:
    frontmatter, _ = parse_frontmatter(path)
    title = frontmatter.get("title") or path.stem.replace("-", " ").title()
    description = frontmatter.get("description", "")
    suffix = f" - {description}" if description else ""
    return f"- [{title}]({rel(path)}){suffix}"


def rebuild_domain_index(domain_path: Path) -> None:
    domain = domain_path.name
    title = domain.replace("-", " ").title().replace("Ai", "AI")
    entries = [index_entry(path) for path in concept_files(domain_path)]
    body = "\n".join(entries) if entries else "No concepts seeded yet."
    text = f"""---
type: Index
title: {title}
description: Domain index for {title} concepts in The Keep.
okf_version: "0.1"
timestamp: 2026-06-25T00:00:00Z
---

# {title}

{body}
"""
    (domain_path / "index.md").write_text(text, encoding="utf-8")


def rebuild_root_index() -> None:
    doctrine = """## Doctrine - `/operating`
- [The Deed](/DEED.md) - the contract every agent reads first
- [soul](/operating/soul.md) - identity
- [soul-loop](/operating/soul-loop.md) - how any agent thinks
- [loop-forge](/operating/loop-forge.md) - the build loop + convergence gate
- [council](/operating/council.md) - the five callable specialists
- [scout](/operating/scout.md) - the ingest producer for new concepts
- [librarian](/operating/librarian.md) - the curator, reconciler, and server
- [prd-agent-run](/operating/prd-agent-run.md) - execution record for the PRD sequence and Keeper gate
- [recon-2026-06-25](/operating/recon-2026-06-25.md) - real-state report and schema convergence record
- [proof-2026-06-25](/operating/proof-2026-06-25.md) - end-to-end Keeper proof and cold-amnesia test
- [invariants](/operating/invariants.md) - the non-negotiables
- [ledger](/operating/ledger.md) - append-only record of Adam's decisions"""
    domains = "\n".join(
        f"- [{path.name}]({rel(path / 'index.md')})" for path in domain_paths()
    )
    text = f"""---
type: Index
title: The Keep - Root Index
description: Progressive-disclosure table of contents for Homesteadai.io's OKF library.
okf_version: "0.1"
timestamp: 2026-06-25T00:00:00Z
---

# The Keep - Root Index

**Boot from [the Deed](/DEED.md) first.** Then load only what you need.

{doctrine}

## Domains
{domains}

*Progressive disclosure: never slurp the whole brain.*
"""
    (ROOT / "index.md").write_text(text, encoding="utf-8")


def duplicate_report() -> list[str]:
    seen: dict[tuple[str, str], Path] = {}
    duplicates: list[str] = []
    for domain_path in domain_paths():
        for path in concept_files(domain_path):
            frontmatter, _ = parse_frontmatter(path)
            title = slugify(frontmatter.get("title") or path.stem)
            key = (domain_path.name, title)
            if key in seen:
                duplicates.append(f"duplicate title in /{domain_path.name}: {seen[key].name} and {path.name}")
            else:
                seen[key] = path
    return duplicates


def archive_marked_concepts() -> list[str]:
    archived: list[str] = []
    for domain_path in domain_paths():
        for path in concept_files(domain_path):
            frontmatter, body = parse_frontmatter(path)
            if frontmatter.get("status", "").lower() not in {"retired", "archived"}:
                continue
            attic_path = unique_path(ROOT / "attic" / domain_path.name / path.name)
            attic_path.parent.mkdir(parents=True, exist_ok=True)
            note = f"\n\n## Archive Note\n\nArchived from `{rel(path)}` by Librarian.\n"
            path.write_text(path.read_text(encoding="utf-8") + note, encoding="utf-8")
            shutil.move(str(path), str(attic_path))
            archived.append(f"{rel(path)} -> {rel(attic_path)}")
    return archived


def copy_raw(source: Path, domain: str) -> tuple[Path, str]:
    raw_dir = ROOT / "_raw" / domain
    raw_dir.mkdir(parents=True, exist_ok=True)
    source_hash = sha256(source)
    destination = unique_path(raw_dir / source.name)
    shutil.copy2(source, destination)
    copied_hash = sha256(destination)
    if copied_hash != source_hash:
        destination.unlink(missing_ok=True)
        raise KeepError(f"copy verification failed for {source}")
    return destination, source_hash


def concept_body(source: Path, raw_path: Path, source_hash: str, text: str, title: str) -> str:
    excerpt_lines = [line.rstrip() for line in text.splitlines() if line.strip()]
    excerpt = "\n".join(excerpt_lines[:40])
    if len(excerpt) > 4000:
        excerpt = excerpt[:4000].rstrip() + "\n[truncated]"

    return f"""# {title}

## Verdict

Captured by Scout from `{source.name}`. Librarian review required before treating
this as resolved memory.

## Source Context

- Original intake file: `{source.name}`
- Raw copy: [{rel(raw_path)}]({rel(raw_path)})
- SHA256: `{source_hash}`

## Extracted Source Text

```txt
{excerpt}
```

## Librarian Notes

- Reconcile against existing concepts before creating siblings.
- Preserve uncertainty; this Scout pass does not canonize final truth.
"""


def scout(source_arg: str) -> Path:
    source = Path(source_arg)
    if not source.is_absolute():
        source = (ROOT / source).resolve()
    if not source.exists() or not source.is_file():
        raise KeepError(f"source file not found: {source_arg}")

    text = read_text(source)
    secret_scan_text(text, str(source))
    domain = infer_domain(source, text)
    if domain not in DOMAINS:
        raise KeepError(f"domain not allowed: {domain}")

    raw_path, source_hash = copy_raw(source, domain)
    title = first_heading(text, source.stem.replace("-", " ").replace("_", " ").title())
    concept_type = infer_type(text)
    description = first_body_line(text)
    slug = slugify(title)
    concept_path = unique_path(ROOT / domain / f"{slug}.md")
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    body = concept_body(source, raw_path, source_hash, text, title)
    frontmatter = f"""---
type: {concept_type}
title: {title}
description: {description}
domain: {domain}
status: candidate
confidence: unknown
source_refs: [{rel(raw_path)}]
tags: [{domain}, scout-capture]
created: {now}
updated: {now}
---

"""
    concept_text = frontmatter + body
    secret_scan_text(concept_text, str(concept_path))
    concept_path.write_text(concept_text, encoding="utf-8")
    return concept_path


def librarian() -> list[str]:
    for domain_path in domain_paths():
        domain_path.mkdir(parents=True, exist_ok=True)

    archived = archive_marked_concepts()
    for domain_path in domain_paths():
        rebuild_domain_index(domain_path)
    rebuild_root_index()

    duplicates = duplicate_report()
    notes: list[str] = []
    if archived:
        notes.extend(f"archived {item}" for item in archived)
    if duplicates:
        notes.extend(f"flagged {item}" for item in duplicates)
    if not notes:
        notes.append("rebuilt indexes; no duplicates or explicit archive markers")
    for note in notes:
        write_log(f"Librarian: {note}")
    return notes


def run_git(args: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=check,
    )


def stage_keeper_outputs() -> None:
    paths = ["index.md", "write-logs", *sorted(DOMAINS)]
    run_git(["add", *paths])


def commit_if_needed(message: str) -> bool:
    stage_keeper_outputs()
    diff = run_git(["diff", "--cached", "--quiet"], check=False)
    if diff.returncode == 0:
        return False
    run_git(["commit", "-m", message])
    return True


def loop() -> list[str]:
    inbox = ROOT / "inbox"
    inbox.mkdir(exist_ok=True)
    sources = sorted(path for path in inbox.rglob("*") if path.is_file())
    if not sources:
        return ["inbox empty; nothing to process"]

    written: list[Path] = []
    processed: list[Path] = []
    for source in sources:
        written.append(scout(str(source)))
        processed.append(source)

    notes = librarian()
    for source in processed:
        source.unlink()

    write_log(
        "Loop: processed "
        f"{len(processed)} inbox file(s), wrote {len(written)} concept(s), "
        "commit=pending"
    )
    committed = commit_if_needed(f"keeper: process inbox {dt.datetime.now(dt.timezone.utc):%Y-%m-%d}")
    return [
        f"processed {len(processed)} inbox file(s)",
        f"wrote {len(written)} concept(s)",
        *notes,
        f"commit {'created' if committed else 'not needed'}",
    ]


def links_from_index(index_path: Path) -> list[tuple[str, Path, str]]:
    if not index_path.exists():
        return []
    links: list[tuple[str, Path, str]] = []
    for line in read_text(index_path).splitlines():
        match = re.search(r"- \[([^\]]+)\]\((/[^)]+)\)(.*)", line)
        if not match:
            continue
        target = ROOT / match.group(2).lstrip("/")
        links.append((match.group(1), target, match.group(3).strip(" -")))
    return links


def choose_domains(query: str) -> list[Path]:
    query_tokens = tokens(query)
    selected: list[Path] = []
    for domain_path in domain_paths():
        domain_tokens = tokens(domain_path.name)
        index_path = domain_path / "index.md"
        index_tokens = tokens(read_text(index_path)) if index_path.exists() else set()
        if query_tokens & (domain_tokens | index_tokens):
            selected.append(domain_path)
    if selected:
        return selected
    return domain_paths()


def excerpt_from_body(body: str, query: str) -> str:
    query_tokens = tokens(query)
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    scored: list[tuple[int, str]] = []
    for line in lines:
        score = len(tokens(line) & query_tokens)
        if score:
            scored.append((score, line))
    if not scored:
        scored = [(0, line) for line in lines[:6]]
    scored.sort(key=lambda item: item[0], reverse=True)
    excerpt = " ".join(line for _, line in scored[:4])
    return excerpt[:800]


def serve(query: str, limit: int = 5) -> str:
    root_index = ROOT / "index.md"
    if not root_index.exists():
        raise KeepError("root index missing")

    query_tokens = tokens(query)
    selected_domains = choose_domains(query)
    candidates: list[tuple[int, Path, str, str]] = []
    for domain_path in selected_domains:
        for title, target, description in links_from_index(domain_path / "index.md"):
            haystack = tokens(f"{title} {description} {target.stem}")
            score = len(query_tokens & haystack)
            if score:
                candidates.append((score, target, title, description))

    candidates.sort(key=lambda item: item[0], reverse=True)
    chosen = candidates[:limit]
    if not chosen:
        domains = ", ".join(f"/{path.name}" for path in selected_domains)
        return f"No matching concepts found. Checked domain indexes: {domains}"

    lines = [f"Answer from The Keep for: {query}", ""]
    for _, path, title, description in chosen:
        if not path.exists():
            lines.append(f"- `{path.with_suffix('').relative_to(ROOT).as_posix()}` TODO link target missing")
            continue
        frontmatter, body = parse_frontmatter(path)
        concept_id = path.with_suffix("").relative_to(ROOT).as_posix()
        summary = description or frontmatter.get("description", "")
        excerpt = excerpt_from_body(body, query)
        lines.append(f"- `{concept_id}` - {title}")
        if summary:
            lines.append(f"  Summary: {summary}")
        if excerpt:
            lines.append(f"  Evidence: {excerpt}")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="keep")
    subcommands = parser.add_subparsers(dest="command", required=True)

    scout_parser = subcommands.add_parser("scout", help="Capture one chosen source file.")
    scout_parser.add_argument("source")
    subcommands.add_parser("librarian", help="Reconcile concepts and rebuild indexes.")
    subcommands.add_parser("loop", help="Sweep /inbox through Scout -> Librarian -> commit.")
    serve_parser = subcommands.add_parser("serve", help="Query by progressive disclosure.")
    serve_parser.add_argument("query", nargs="+")

    args = parser.parse_args(argv)
    try:
        if args.command == "scout":
            output = scout(args.source)
            print(f"Scout wrote {rel(output)}")
            return 0
        if args.command == "librarian":
            for note in librarian():
                print(note)
            return 0
        if args.command == "loop":
            for note in loop():
                print(note)
            return 0
        if args.command == "serve":
            print(serve(" ".join(args.query)))
            return 0
    except KeepError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
