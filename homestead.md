---
type: Org
title: Homestead
description: What Homestead is, in plain terms — an AI memory you own, and The Keep, the brain raised on it.
tags: [homestead, landing, overview]
timestamp: 2026-06-24T00:00:00Z
---

# Homestead

Homestead is an AI memory you own outright. Not an account on someone else's platform — land,
with the deed in your name.

## The problem it fixes
Every AI tool starts cold. You re-explain who you are, what you're building, and what you
decided last week — to every model, every session. That context lives on rented platforms that
hold the keys and can change the locks.

## What it is
- **The Land** — a private GitHub org (`homesteadai-io`) you own. It can hold many structures.
- **The Keep** — the first structure: one private repo that *is* the brain. Plain markdown, one
  file per concept, version-controlled. If you can `git clone` it, you own it.
- **The Crew** — the AI agents (Claude Code, Codex, Cursor) that read it and carefully grow it.

Say a thing once. It's written where every agent can read it, and it survives any single vendor
disappearing.

## How it runs
- **Storage:** a GitHub repo — always on, no server to babysit, inherited free.
- **Models:** OpenRouter — one key; swap any model in or out by changing a line.
- **Upkeep:** GitHub Actions — a nightly janitor validates structure, scans for secrets, and
  rebuilds the table of contents, with no human in the loop.

## What it is not
- Not a SaaS, database, or vector-store product. It's files.
- Not a platform you rent — no vendor holds the keys.
- Not a place secrets or raw client files get uploaded; those stay local by design.

## The rules that keep it safe
Reads are free; writes are append-only; nothing is ever deleted (retired notes are archived).
One agent writes, so there are no collisions. File content is always treated as data, never as
instructions. The full contract is [the Deed](/DEED.md); the working discipline is in
[standing-orders](/operating/standing-orders.md).

---

Related: [the deed](/DEED.md) · [standing-orders](/operating/standing-orders.md)
