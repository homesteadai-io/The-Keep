#!/usr/bin/env python3
"""The Keep — the gate. OKF conformance + secret scan. Pure stdlib, no network, no LLM.

Single source of truth for both workflows:
  - okf-validate.yml  (on: push / pull_request)  — the required status check
  - nightly-sweep.yml (on: schedule / dispatch)  — re-runs the same gate after sweeping

Exit non-zero on any hard failure. Reserved files are exempt from the `type` rule.
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Files that carry no OKF `type` by design (containers, redirects, the contract).
RESERVED = {
    "index.md", "log.md", "ledger.md", "README.md",
    "AGENTS.md", "CLAUDE.md", "DEED.md",
}
# Directories never scanned for OKF conformance.
OKF_SKIP_DIRS = {".git", "_raw", "attic"}
# Directories excluded from the secret scan (workflow/tooling hold the patterns themselves).
SECRET_SKIP_DIRS = {".git", "_raw", ".github", "tools"}

FM_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)  # LF-only: CRLF blobs would (correctly) fail
TYPE_RE = re.compile(r"^type:\s*(\S.*)$", re.MULTILINE)

SECRET_PATTERN = re.compile(
    r"(AKIA[0-9A-Z]{16}"                       # AWS access key id
    r"|sk-[A-Za-z0-9]{20,}"                    # OpenAI-style key
    r"|-----BEGIN [A-Z ]*PRIVATE KEY-----"     # PEM private key
    r"|xox[baprs]-[0-9A-Za-z-]+"               # Slack token
    r"|ghp_[A-Za-z0-9]{36})"                   # GitHub PAT
)


def okf_validate():
    fails = []
    for p in ROOT.rglob("*.md"):
        rel_parts = p.relative_to(ROOT).parts
        if any(part in OKF_SKIP_DIRS for part in rel_parts):
            continue
        if p.name in RESERVED:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        m = FM_RE.match(text)
        if not m:
            fails.append(f"{p.relative_to(ROOT).as_posix()}: missing YAML frontmatter")
            continue
        tm = TYPE_RE.search(m.group(1))
        if not tm or not tm.group(1).strip():
            fails.append(f"{p.relative_to(ROOT).as_posix()}: missing or empty `type`")
    return fails


def secret_scan():
    hits = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel_parts = p.relative_to(ROOT).parts
        if any(part in SECRET_SKIP_DIRS for part in rel_parts):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="strict")
        except (UnicodeDecodeError, OSError):
            continue  # binary / unreadable — nothing to scan
        for m in SECRET_PATTERN.finditer(text):
            hits.append(f"{p.relative_to(ROOT).as_posix()}: possible secret ({m.group(0)[:8]}…)")
    return hits


def main():
    okf = okf_validate()
    secrets = secret_scan()

    if okf:
        print("OKF validation failed:")
        for f in okf:
            print("  -", f)
    else:
        print("OKF OK — every non-reserved concept carries a type.")

    if secrets:
        for s in secrets:
            print(f"::error::{s}")
        print("Secret scan FAILED — quarantine, do not commit.")
    else:
        print("Secret scan clean.")

    sys.exit(1 if (okf or secrets) else 0)


if __name__ == "__main__":
    main()
