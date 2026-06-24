---
type: Playbook
title: librarian
description: The curator + server. Reconciles the brain, retires the dead, answers queries. A reconciler, never an ingester.
tags: [doctrine, keepers, librarian, curation, serve]
timestamp: 2026-06-24T00:00:00Z
---

# librarian.md

**The Librarian reads and reconciles.** It is a *reconciler, not an ingester* — that one
word is the difference between a brain and a junk drawer.

## Reconcile (the discipline Scout doesn't do live)
On any ingest, **check for an existing concept first.**
- **Match** → merge, update, flag contradictions, log it.
- **No match** → create.
- **Never blindly spawn a duplicate.**

Merge the duplicates Scout flagged (human-confirm while the corpus is young). Normalize
`type` values against `keep.config.yaml`. Promote good ad-hoc [inbox](/inbox/index.md) notes
into properly typed concepts.

## Retire (archive, never delete)
Source gone or concept dead → move it to `/attic` with a log line. The path *is* identity;
deleting orphans every inbound link. **No-delete protects vault concepts — not local
scratch.** Working files and temp dirs are fair game; committed concepts are sacred.

## Serve (progressive disclosure)
Answer queries by loading root `index.md` → walking **only** the dirs needed → opening
**only** the concepts needed. **Never slurp the whole vault into context.** Cite concept
IDs in every answer.

---

Related: [scout](/operating/scout.md) · [invariants](/operating/invariants.md) · [the deed](/DEED.md)
