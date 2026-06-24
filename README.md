# The Keep

**Homesteadai.io OKF Library — Adam's owned AI brain.**

A private, git-versioned library of OKF markdown. One repo, read by every agent
(Codex, Claude Code, Cursor) so each session starts already knowing Adam's world
instead of being re-briefed from scratch.

> Platforms rent you a desk and keep the keys. Homestead is the land. Say a thing
> once, it's written where every agent reads it, and the deed is in Adam's name.

## Read this first

**Every agent boots from [`/DEED.md`](/DEED.md).** It is the contract — identity,
invariants, vocabularies, lanes, loop, and build order. If a choice violates the
Deed, the choice is wrong.

## Structure

```
DEED.md            # the contract — read first
index.md           # root table of contents (OKF)
AGENTS.md          # boot redirect (Codex / generic)
CLAUDE.md          # boot redirect (Claude Code)
keep.config.yaml   # types, domains, guardrails, model port (OpenRouter)
operating/         # doctrine: soul, soul-loop, loop-forge, council, invariants, ledger
lyhna/             # memory domain (sealed as content — never plumbing)
people/            # contacts
attic/             # retired concepts (archive, never delete)
_raw/              # immutable source copies — GITIGNORED, never pushed
```

## Where it runs

- **Brain:** this GitHub repo. Always on, inherited free. No server to babysit.
- **Model port:** OpenRouter — one key, every model, dropped in/out by config.
- **Janitor:** GitHub Actions — OKF validate + secret scan on every commit.

Zero servers in v1. The repo *is* the always-on.
