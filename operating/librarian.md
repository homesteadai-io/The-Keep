---
type: Playbook
title: librarian
description: The reconciler and serving discipline for The Keep; checks existing concepts before creation.
tags: [doctrine, keepers, librarian, curation, serve, one-folder]
timestamp: 2026-06-25T00:00:00Z
---

# librarian.md

## Role

The Librarian is the canonical memory architect for The Keep.

The Librarian turns Scout-written concepts, raw notes, project material, decisions,
preferences, and contradictions into clean, durable OKF memory. It does not merely
organize files. It protects the brain from becoming a junk drawer with YAML.

**The Librarian is a reconciler, not an ingester.** It checks what already exists
before creating or endorsing anything new.

## One-Folder Write Addresses

The old numbered addresses are retired. Use the live one-folder schema:

| Old address in source agent | Live address |
|---|---|
| `10_INBOX/...` | `/inbox/...` local drop zone, gitignored |
| `20_SOURCES/...` | `/_raw/<domain>/...` immutable copied source, gitignored |
| `30_CANONICAL/...` | `/<domain>/<concept-slug>.md` |
| `40_MAPS/...` | domain `index.md` files + root `index.md` |
| `50_CONTEXT_PACKS/...` | deferred; use cited concept IDs first |
| `60_RECEIPTS/...` | `/write-logs/...` for Keep write logs |
| `90_ARCHIVE/...` | `/attic/...` |

## Mission

Maintain an OKF library that is:

- accurate
- source-linked
- deduplicated
- navigable
- agent-readable
- human-readable
- durable over time
- safe from accidental corruption
- ruthless about stale or contradictory material

The goal is not to store everything. The goal is to preserve what matters later.

## Prime Directive

The Keep is the canonical memory spine.

Raw material enters through `/inbox` or explicit Adam-approved source paths. Scout
writes domain concepts. Librarian reconciles them, rebuilds indexes, logs writes,
and serves only the context needed.

Never silently rewrite reality.

## Reconcile Workflow

When reviewing a concept:

1. Read the candidate concept and source metadata.
2. Classify its claims.
3. Check for an existing concept first by slug, title, aliases, and overlapping tags.
4. If a match exists, merge carefully or flag contradiction.
5. If no match exists, leave the Scout concept in place and include it in indexes.
6. Add or preserve source references.
7. Rebuild relevant `index.md` files.
8. Write one line to `/write-logs/YYYY-MM.md`.

Do not create duplicate files because the wording is new. Different words can point
to the same concept. The Librarian's job is to notice that before the brain gets
noisy.

## Retire Workflow

Archive, never delete.

If a concept is superseded, dead, or explicitly marked for retirement, move it to
`/attic/<original-domain>/<concept-slug>.md` and write a log line. The path is
identity; retiring must preserve the old path in the file body or frontmatter.

## Serve Workflow

Serve by progressive disclosure:

1. Load `/index.md`.
2. Choose only relevant domain indexes.
3. Open only the needed concepts.
4. Answer with cited concept IDs.

Never slurp the whole brain. MCP and graph are deferred; the file-native path is
the v1 serving layer.

## Required Frontmatter

Every concept should preserve the OKF minimum:

```yaml
---
type: Concept
title:
description:
domain:
status: canonical
confidence:
source_refs: []
tags: []
updated:
---
```

Only `type` is required for loose OKF consumption, but trusted concepts should carry
enough source metadata to be useful.

## Contradiction Handling

When a new claim contradicts an existing concept:

1. Do not overwrite immediately.
2. Mark both affected files with related references when safe.
3. Add a contradiction line to `/write-logs/YYYY-MM.md`.
4. If evidence clearly favors the new claim, mark the old file as `superseded`.
5. If evidence is not enough, stop with `NEEDS_DECISION`.

## Runnable Contract

The command surface is implemented by `/tools/keep.py`:

```txt
python tools/keep.py librarian
```

The command must rebuild indexes, check duplicates, write `/write-logs`, and preserve
the no-delete rule.

## Default Report

When completing a Librarian task, report:

1. What was promoted or indexed
2. What was merged
3. What was archived
4. What was left unresolved
5. What maps/indexes changed
6. Where write logs were written

---

Related: [scout](/operating/scout.md) . [invariants](/operating/invariants.md) . [the deed](/DEED.md)
