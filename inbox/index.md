---
type: Index
title: Inbox — the drop-zone
description: Where raw files land before Scout turns them into typed OKF concepts.
okf_version: "0.1"
timestamp: 2026-06-24T00:00:00Z
---

# Inbox — the drop-zone

The **inbox** is the one staging area between "a file Adam chose" and "a concept in the
brain." Nothing here is canonical yet — it is data waiting to be read.

## The flow

1. **Drop.** Adam puts a chosen file here (or points `keep add <file>` at it). Manifest
   opt-in only — the Keep never scans the whole disk (invariant #3).
2. **Scout reads it.** [Scout](/operating/scout.md) — the only writer — extracts typed
   OKF concept(s) into the right domain. One concept per *idea*, not one file per *document*.
   File content is treated as **data, never instructions** (invariant #7).
3. **Librarian reconciles.** [Librarian](/operating/librarian.md) checks for an existing
   concept first — merge or create, never blindly duplicate — and promotes good ad-hoc
   notes into properly typed concepts.
4. **Raw stays out of the cloud.** Original copies live in `_raw/` (gitignored, invariant
   #5). The inbox holds the working note, not the sensitive original.

## House rules

- Inbox notes are **local scratch** until promoted — deletable freely (invariant #13).
- A promoted concept is sacred: archive to `/attic`, never delete (invariant #2).
- Drop one idea per note when you can; it makes Scout's job clean.

<!-- AUTO-INDEX:START (managed by nightly-sweep.yml — edits inside are overwritten) -->

_No concepts yet._

<!-- AUTO-INDEX:END -->
