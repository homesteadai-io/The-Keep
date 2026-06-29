---
type: Truth
title: The Keep Truth
description: Current plain-English truth of The Keep, Homestead Door, and proven agent boot behavior after the June 2026 build arc.
tags: [homestead, keep, truth, door, agents, proof]
timestamp: 2026-06-29T00:00:00Z
---

# The Keep Truth

This is not a handoff.

This is the current truth of what The Keep is, what Homestead does with it, and what was proven by live tests after the June 2026 build arc.

## One Sentence

The Keep is Adam's owned, git-readable memory shelf, and Homestead is the live operating spine that lets fresh agents boot from that memory, keep project contexts separate, cite concept IDs, and preserve useful work without becoming autonomous.

## The Plain Model

The system now has two pieces that must not be blurred:

| Thing | Plain meaning | Source of truth |
|---|---|---|
| The Keep | Adam's shared OKF memory shelf: markdown concepts, doctrine, indexes, project context, output bundles | `homesteadai-io/The-Keep` |
| Homestead Private OS | The live API/control spine that lets agents boot, inspect capabilities, read concepts, write approved output capsules, and prove behavior | `homesteadai-io/homestead-private-os-infra` on Hetzner |

The Keep is not the server. The live API is not the memory. The Keep stores the durable context; Homestead serves it to agents through a controlled Door.

## What The Keep Is

The Keep is a private, git-native memory repo.

It is built from plain files:

- `DEED.md` for root doctrine.
- `AGENTS.md` for how agents behave when they enter the repo.
- domain folders for project and concept lanes.
- `/operating` for doctrine such as soul, loop, council, invariants, and ledger.
- `/System Outputs` for durable Homestead output capsule bundles.

The Keep is meant to solve a simple problem:

```text
Adam should not have to re-brief every fresh agent from scratch.
```

Useful context gets parked once, filed cleanly, and made readable by future agents.

## What The Keep Is Not

The Keep is not:

- a secret vault
- a public SaaS product
- a vector database
- a dashboard
- a runner
- a scheduler
- a place for autonomous agents to claim work
- a replacement for Adam's authority
- a dumping ground for raw transcripts, tokens, prompts, or private completion captures

The Keep is storage and memory. It is not permission, autonomy, or execution.

## The Door

The Door is the human trigger that lets a fresh agent boot into Homestead.

Preferred phrase:

```text
@Homestead
```

Equivalent text aliases:

```text
Boot Homestead.
/homestead
/boot-homestead
$homestead
```

Important distinction:

- `@Homestead` is the preferred plain-chat alias.
- `$homestead` is the local Codex skill trigger.
- `/homestead` and `/boot-homestead` are documented text aliases, not guaranteed native slash-command dropdown items.
- All aliases mean the same thing: call the live private Homestead Door first.

The canonical Door behavior is:

```text
Call the live private Homestead API first.
Use local Keep doctrine only as supporting context after the live Door answers.
Do not substitute a local Deed-only boot for the Door.
```

## What A Fresh Agent Does Now

When a fresh agent receives `@Homestead`, it should:

1. Call the live Door.
2. Read OS status and capabilities.
3. Read the project registry.
4. Read Keep concepts through the concept surface.
5. Keep project contexts separate.
6. Cite `concept_id` values when answering from Keep content.
7. Treat Adam as authority.
8. Treat disabled capabilities as unavailable.

The live Door currently proves two project lanes:

- `homestead-private-os`
- `creative-coatings`

## Proven Concept Surface

Homestead indexes existing Keep markdown as read-only concepts.

Each concept summary includes:

```text
concept_id
project_id
title
source_keep_path
snippet
updated_at
```

Concept IDs are stable citations from Keep-relative paths. They are for reference and continuation, not authority.

Read-only surfaces:

```text
GET /api/keep/concepts
POST /api/keep/concepts/search
GET /api/keep/concepts/{concept_id}
```

MCP equivalents:

```text
homestead.keep_concepts
homestead.keep_concept_search
homestead.keep_concept_read
```

Known proven concept IDs include:

| Project | Meaning | Concept ID |
|---|---|---|
| `homestead-private-os` | The Homestead Deed | `concept-deed-571b2b47` |
| `homestead-private-os` | Homestead overview | `concept-homestead-cdd07bcc` |
| `homestead-private-os` | Homestead health latest | `concept-system-receipts-homestead-health-homestead-latest-7d8b5c17` |
| `homestead-private-os` | Output capsule acceptance | `concept-system-outputs-homestead-private-os-2026-06-28-output-capsule-acceptance-20260628-222457-index-c40f3eb1` |
| `creative-coatings` | Creative Coatings Door ingest capsule | `concept-system-outputs-creative-coatings-2026-06-28-door-ingest-creative-coatings-capsule-59a7f1b6` |

## Output Capsules

Output capsules are durable bundles of useful work and continuation context.

Approved lane:

```text
/System Outputs/{project_id}/{YYYY-MM-DD}-{slug}/
```

Required bundle shape:

```text
index.md
HANDOFF.md
handoff.json
CAPSULE.md
capsule.json
next-ai-prompt.md
okf/
pam/
```

What capsules are for:

- preserving useful work
- preserving continuation context
- linking work to project, command, or session context
- making later agents smarter without Adam re-explaining the work

What capsules are not:

- receipts
- raw model transcripts
- secret stores
- prompt dumps
- autonomous work claims

Receipts remain separate proof of system behavior. Output capsules preserve useful work.

## Receipts

Receipts prove what the system did.

They are separate from output capsules.

This distinction matters:

```text
/System Receipts = proof lane
/System Outputs = durable work/capsule lane
```

Do not put output capsules inside `/System Receipts`.

Do not treat receipts as project memory capsules.

## Policy Gate

Manual operations and output writes now sit behind an approval/policy layer.

The policy gate answers:

```text
who/what is asking
what action is requested
whether that surface is allowed
whether Adam confirmation is required
```

The policy gate is not RBAC, OAuth, users, roles, or an admin system. Adam is still the authority. The gate is a guardrail around manual ops and write surfaces.

## Current Live Capabilities

As of the last live verification on 2026-06-29:

| Capability | Status |
|---|---|
| Door / agent boot | enabled |
| Keep concepts | enabled |
| Output capsules | enabled |
| Ops policy gate | enabled |
| Manual ops | enabled, gated |
| Production model gateway | `direct` |
| Runner | disabled |
| Scheduler | disabled |
| Local mode | disabled |
| Dashboard | disabled |
| Alerts | disabled |
| Autonomous claiming | disabled |

Public ports checked:

```text
5.78.206.130:8088 timeout
5.78.206.130:4000 timeout
5.78.206.130:3000 timeout
5.78.206.130:9090 timeout
```

The private Door is reachable through the private network, not public exposure.

## What Was Proven

The release `v0-door-cold-boot` proved this:

```text
A fresh agent can enter with one phrase, call the live Door, read real Keep concepts, keep Homestead and Creative Coatings separate, and answer Adam-readable questions with concept IDs.
```

The accepted proof questions were:

1. What is Homestead, and what should an agent read first before working?
2. What is the current operating mode, and which capabilities are disabled?
3. What does Homestead use output capsules for, and where are they stored?
4. What is the Creative Coatings powder scheduler, and what problem does it solve?
5. What is the difference between Core Dump Inbox and Schedule Intake Inbox?
6. Is Creative Coatings part of the Homestead runtime, or is it a separate project context?

The final fresh-agent proof answered:

- Homestead is Adam's private operating spine / owned memory system.
- Homestead is manual-only.
- Runner, scheduler, dashboard, alerts, local mode, and autonomous claiming are disabled.
- Output capsules live under `/System Outputs/{project_id}/{YYYY-MM-DD}-{slug}/`.
- Creative Coatings is a separate powder-schedule workflow project.
- Core Dump Inbox is clean plant/open-order data for the In Process candidate pool.
- Schedule Intake Inbox is messy human scheduling input.
- Creative Coatings is not the Homestead runtime.

## The Creative Coatings Boundary

Creative Coatings is a separate project context indexed by Homestead.

It is not:

- Homestead runtime
- Homestead scheduler
- Homestead dashboard
- Homestead local mode
- Homestead runner

It is:

- a powder-schedule business workflow
- a weekly powder board and scheduling context
- a project lane that Homestead can read and cite

The final proof required the agent to keep this boundary straight.

## The Invocation Truth

Adam should be able to type:

```text
@Homestead
```

Then type normal English:

```text
Keep this as a concept:
[plain English concept]
Apply this to [project].
```

or:

```text
File this decision:
[plain English decision]
Apply this to [project].
```

Current truth:

- The Door boot is proven.
- The alias is documented and skill-backed.
- `$homestead` is the native Codex skill-style trigger.
- `@Homestead` is the preferred human-facing text alias.
- `/homestead` is a text alias unless Codex adds native custom slash-command registration.

If the gated concept/decision write surface is unavailable, the agent must say so plainly and not fake a write.

## What Is Not Built Yet

The following are intentionally not built:

- autonomous runner
- scheduler
- dashboard
- alerts
- local-mode autonomy
- local model routing
- workflow engine
- multi-tenant permissions
- user accounts
- OAuth/admin system
- native custom slash-command dropdown registration

The system is allowed to be useful without pretending to be autonomous.

## How Adam Should Think About It

The Keep is the shelf.

Homestead is the Door and control spine.

Concept IDs are labels on the shelf.

Output capsules are durable bundles of useful work.

Receipts are proof that the system behaved.

Adam is the authority.

Agents are operators.

The correct feeling is:

```text
Adam types a plain phrase.
Codex boots through the live Door.
The agent reads the right shelf.
The agent cites what it used.
The agent writes only through approved gates.
The next agent starts smarter.
```

That is the thing that was built.

## Current Source Pointers

The important files and surfaces are:

```text
The-Keep:
/DEED.md
/AGENTS.md
/THE-KEEP-TRUTH.md

Homestead infra:
/docs/DOOR-COLD-BOOT.md
/docs/OUTPUT-CAPSULE-WRITE-POLICY.md
/docs/ACCEPTANCE-TESTS.md

Codex local:
C:\Users\Adam\.codex\skills\homestead\SKILL.md
```

## Final Truth

The Keep is no longer just a folder of good intentions.

It is now connected to a live Door that a fresh agent can use, a concept index that returns real citation IDs, a gated output lane that preserves durable work, and a proof loop that demonstrated Homestead and Creative Coatings can stay separate in a cold boot.

It is not finished as a full personal OS.

But the core thing is alive:

```text
One phrase can wake the system.
The system can orient a fresh agent.
The agent can cite real memory.
Useful work can become durable.
Adam stays in charge.
```
