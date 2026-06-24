---
type: Playbook
title: loop-forge
description: The build loop and convergence gate — how WORK gets made on the land.
tags: [doctrine, loop, governance, homestead]
timestamp: 2026-06-23T00:00:00Z
---

# loop-forge.md

How **work** gets built. (Distinct from `soul-loop`, which is how any agent *thinks*.)
Default to a convergence loop, not a single pass. A single pass is "pizza in, pizza out" —
it anchors on the first framing and ships shallow.

## The Four Hats (run in sequence — one agent wearing them, or several)

- **Planner** — frames the work, names the smallest viable target, lists the unknowns. Does **not** pre-seed the answer; a pre-baked answer makes every later pass anchor on it.
- **Builder** — produces the actual artifact (code, schema, doc).
- **Adversary** — attacks it: what's missing, what overclaims, what breaks, what drifts from doctrine. Holds the kickback edge — can send work back to Builder or Planner with specific named failures.
- **Resolver** — decides. Either the work clears the gate, or it returns `NEEDS_DECISION` and escalates to Adam rather than guessing.

## Convergence Gate — when to STOP

| Exit | Meaning | Action |
|---|---|---|
| ✅ Converged | Artifact stable; Adversary finds nothing load-bearing; doctrine holds | Ship it |
| 🟡 NEEDS_DECISION | A real fork only Adam can call | Stop, surface it, do not guess |
| 🔻 Diminishing returns | Pass N+1 ≈ pass N; polish isn't improving it | Stop, converge |
| ⛔ Max passes | Cap the loop (default 3–4); not converged | Escalate, don't spin |
| ❌ Hard failure | The premise itself is wrong | Kill it, report why |

## Loop Guards
- **Anti-anchor:** frame the problem for the Planner, don't seed the answer.
- **Diminishing-returns:** if a pass stops improving the artifact, you're done.
- **Tripwire:** if the artifact grows past smallest-viable, the Adversary kicks it back. Scope creep is a load-bearing failure.

## Vocabulary Seal
Loop activity is logged as a **trace** (`loop_trace` / `gate_trace` / `run_trace`) — Loop Forge's word.
**Not** a *receipt* (Lyhna's word). **Not** a *ledger* entry (Homestead's word, for Adam's decisions).
Keep the three sealed. See [the deed](/DEED.md) §4.

---

Related: [soul-loop](/operating/soul-loop.md) · [council](/operating/council.md) · [invariants](/operating/invariants.md)
