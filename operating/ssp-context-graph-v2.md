---
type: Concept
title: SSP Context Graph v2
description: SSP as The Keep's deterministic Librarian match key and first self-scoring context-graph primitive.
tags: [homestead, keep, librarian, ssp, context-graph, reconcile, deterministic-edges]
timestamp: 2026-06-29T00:00:00Z
---

# SSP Context Graph v2

## Verdict

The Keep today is a self-storing context graph.

SSP is the first piece that can make it self-scoring without turning it into a vector-memory product, dashboard, runner, or autonomy system.

The move now is narrow:

```text
Use SSP as the Librarian's deterministic match key.
```

Do not build the full scoring layer yet.

## Reframe

Most small-business context graphs are memory systems:

```text
store traces
retrieve similar context later
```

The Keep should move differently:

```text
store owned concepts
compute deterministic edges
surface coherence or drift
```

The useful distinction:

| Crowd context graph | The Keep with SSP |
|---|---|
| remembers | grades |
| fuzzy vector similarity | deterministic grouping key |
| similar past decision | concept bucket, contradiction trigger, coherence signal |
| text blob in vector DB | owned append-only markdown concept |
| commodity memory | portable deterministic measurement |

## What SSP Means Here

SSP is a deterministic grouping key for concepts and decisions.

It answers:

```text
Is this the same kind of concept, decision, or operating judgment as something already in The Keep?
```

This is the missing rigor behind the Librarian's existing promise:

```text
reconcile before spawning a new concept
```

Without SSP, matching can degrade into title vibes, manual eyeballing, or fuzzy retrieval.

With SSP, matching becomes a pure function.

## Proposed Keep SSP Shape

The Keep SSP should be computed from stable fields, not from embeddings.

Initial grouping key:

```text
domain | concept_type | decision_kind | doctrine_epoch
```

Field meanings:

| Field | Meaning | Example |
|---|---|---|
| `domain` | project or operating lane | `homestead-private-os`, `creative-coatings`, `frostbite` |
| `concept_type` | kind of memory | `concept`, `decision`, `policy`, `playbook`, `output-capsule` |
| `decision_kind` | what sort of judgment this represents | `pricing`, `schedule-intake`, `door-policy`, `agent-routing`, `reconcile-rule` |
| `doctrine_epoch` | version of the rules under which it should be judged | `keep-v1`, `door-v0`, `output-capsules-v0` |

Computed form:

```text
ssp_key = normalize(domain) + "|" + normalize(concept_type) + "|" + normalize(decision_kind) + "|" + normalize(doctrine_epoch)
ssp_hash = sha256(ssp_key)
```

The readable key is for humans. The hash is for stable machine edges.

## What SSP Unlocks Now

SSP can land before the Agent Registry and before any scoring dashboard.

Near-term value:

- deterministic duplicate detection
- cleaner reconcile-before-spawn behavior
- automatic contradiction surfacing inside a bucket
- concept edges without vector search
- better Librarian review queues
- more useful concept IDs and continuation paths

The important trigger:

```text
If two concepts share an SSP bucket but disagree on an active claim, surface a contradiction for Librarian review.
```

Do not silently overwrite.

Do not merge by vibes.

Do not invent a stronger claim than the sources support.

## Ranked 6/7 Primitives For The Keep

| Rank | Primitive | Keep role | When |
|---:|---|---|---|
| 1 | SSP | Librarian match key and deterministic concept edges | now |
| 2 | Reducer | domain coherence score | after Agent Registry / decision stream |
| 3 | Epoch pin | doctrine-versioned scoring so rule changes do not look like drift | with Reducer |
| 4 | Snapshot + signed node | sealed Keep state and portable capsule proof | later |

Only SSP belongs in The Keep now.

Reducer, epoch pin, and snapshot/signing are real but queued.

## Why Not Reducer Yet

Reducer is the larger self-scoring move:

```text
fold a domain's concepts and write-logs into a coherence verdict
```

Example future output:

```text
creative-coatings: stable and tightening
frostbite: drifting, 3 unreconciled pricing decisions
```

That is valuable, but it needs a real decision stream.

The Keep currently has durable concepts and output capsules. It does not yet have enough live, policy-gated decision events to make a coherence score meaningful.

A score over a thin stream is theater.

SSP first.

Reducer later.

## Where SSP Slots

Build order:

```text
Cold boot proof
  -> Agent Registry
  -> SSP edges for Librarian match key
  -> Witness or decision-flow events
  -> Reducer coherence score
  -> Epoch pin
  -> Snapshot/signing
```

SSP can start as a Librarian-side computed field, not a product surface.

## Guardrails

SSP must not import unwanted machinery.

Do not add:

- Lyhna runtime
- witness fields
- receipt vocabulary
- authority machinery
- vector database dependency
- dashboard
- runner
- scheduler
- autonomous claiming

Lift the math.

Keep the vocabulary Keep-native.

## Keep-Native Names

Use these words:

| Word | Use |
|---|---|
| `ssp_key` | readable deterministic grouping key |
| `ssp_hash` | stable hash of the grouping key |
| `ssp_bucket` | all concepts sharing the same key |
| `contradiction_candidate` | bucket item that appears to conflict with another active claim |
| `librarian_review` | human/agent review queue for reconcile decisions |

Avoid importing non-Keep grammar for this layer.

## First Implementation Shape

The first SSP implementation should be tiny.

Inputs:

```text
concept frontmatter
source_keep_path
project/domain
type
tags
title
optional decision_kind
optional doctrine_epoch
```

Outputs:

```text
ssp_key
ssp_hash
ssp_bucket
possible_duplicates
possible_contradictions
```

The first acceptance test should not need models.

It should prove:

```text
same stable fields -> same SSP hash
changed doctrine_epoch -> different SSP hash
same bucket + conflicting active claims -> contradiction candidate
different domain -> different bucket
```

## Final Truth

The Keep's current moat is not that it remembers.

Everyone is building memory.

The Keep's stronger path is that it can become a deterministic, portable context graph that grades whether a domain's judgment is cohering or drifting.

SSP is the first brick because it improves the Librarian immediately:

```text
reconcile before spawning
compute edges before retrieval
surface contradictions before rot
```

That is Context Graph v2 for The Keep.

