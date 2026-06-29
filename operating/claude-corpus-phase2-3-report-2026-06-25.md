---
type: Session
title: Claude Corpus Phase 2/3 Mine and Reconcile Report
description: Full-text concept mining and reconciliation report for Adam's Claude export.
tags: [homestead, claude-export, mining, reconciliation]
timestamp: 2026-06-25T00:00:00Z
---

# Claude Corpus Phase 2/3 Mine and Reconcile Report

## Verdict

Phase 2/3 mined the tightened manifest without mining `NEEDS_DECISION` chats. Full chat/doc text was scanned against explicit concept patterns, repeated signals were collapsed into one concept per idea, and redacted evidence bundles were written under ignored `/_raw`.

## Counts

- Concepts in this mine: 73
- Concept files created: 73
- Existing concept path merges/skips: 0
- Source-to-concept cluster merges: 5010
- Concepts with contradiction flags: 24
- Concepts with explored/rejected signals: 72

## Per-Domain Concept Counts

| Domain | Concepts mined | New files created |
|---|---:|---:|
| `creative-coatings` | 9 | 9 |
| `frostbite` | 12 | 12 |
| `homesteadai-io` | 10 | 10 |
| `ai-theory-builds` | 10 | 10 |
| `keryke` | 14 | 14 |
| `lyhna` | 11 | 11 |
| `personal` | 7 | 7 |

## Skip-Noise Check

- Skip-noise chats checked: 120
- Short-but-real chats rescued: 1

| Title | Routed domain | Why rescued |
|---|---|---|
| Unable to access X post content | `keryke` | nonblank-title-with-substance |

## Frontier Sanity: Frostbite -> Keryke Bleed

These are the five largest Keryke-routed chats that still contain Frostbite vocabulary. They are shown so Adam can confirm the Frostbite drop was real bleed, not stolen signal.

| Chat | Messages | Keryke hits | Frostbite hits | Route reason |
|---|---:|---|---|---|
| 5.23 MCP Proxy Adapter | 433 | keryke, arlo inc, chione, arlo | frostbite, frostbite feeders, mice | content-overrode-title |
| Arlo Inc v.0.3 progress update | 365 | arlo inc, arlo | frostbite | title-map |
| Arlo/Lyhna first tenant | 306 | arlo inc, arlo build, arlo, ai os | frostbite, frostbite feeders, reptile, snake | title-map |
| 5.17 Keryke Stand-up | 287 | keryke, arlo inc, tabula, chione, chione hermes | frostbite, frostbite feeders, feeder rodent, feeder rodents | title-map |
| Arlo Web game called "Frostbite HQ" | 271 | arlo build, arlo | frostbite, frostbite feeders, feeder rodent, feeder rodents, reptile | title-map |

## Contradiction Flags

- `homesteadai-io/agents-instructions-and-project-doctrine`: Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `homesteadai-io/claude-corpus-ingest`: Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `homesteadai-io/cold-amnesia-proof`: Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `homesteadai-io/keep-deed-and-domain-spine`: Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `homesteadai-io/local-codex-agent-operations`: Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `homesteadai-io/openrouter-model-port`: Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `homesteadai-io/prompt-and-handoff-artifacts`: Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `homesteadai-io/scout-librarian-keeper-loop`: Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `homesteadai-io/soul-loop-and-council-reasoning`: Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `homesteadai-io/zero-server-git-native-architecture`: Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/agent-observability-and-runaway-prevention`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/arlo-architecture-and-buildout`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/crimson-desert-companion`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/frostbite-hq-bleed-boundary`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/keryke-company-lineage`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/lyhna-integration-as-consumer`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/memory-second-brain-and-obsidian`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/model-choice-and-cost-control`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/room-spine-and-repurposing-room`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/small-business-ai-operator-substrate`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/tabula-and-chione-lineage`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/talaria-browser-os`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/voice-avatar-and-interface-identity`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.
- `keryke/vps-and-local-infrastructure`: Contains Frostbite terms inside Arlo/Keryke source; preserve as Keryke bleed unless Adam redirects. / Supabase appears in source history; do not resurrect retired Homestead stack without Adam's call.

## Phase 4: Reconciled Brain Counts

These are total concept files after reconciliation, including the small pre-existing
seed concepts plus the corpus mine.

| Domain | Total concept files |
|---|---:|
| `creative-coatings` | 9 |
| `frostbite` | 12 |
| `homesteadai-io` | 11 |
| `ai-theory-builds` | 10 |
| `keryke` | 14 |
| `lyhna` | 12 |
| `personal` | 8 |

## Phase 4: Cold-Amnesia Test

Result: pass. The file-native `serve` path answered from domain indexes and concept
files after the Librarian rebuilt indexes.

### Keryke

Question: What is Keryke and how do Arlo, Talaria, Tabula, and Crimson Desert fit?

Answer from brain: Keryke is the company/library lane carrying the former Arlo
lineage. Arlo architecture and buildout are the dominant source lineage; Talaria is
the browser/super-app product surface; Tabula and Chione are Keryke lineage/product
infrastructure rather than active Homestead stack; Crimson Desert is a Keryke
companion product lane. Cited concepts included `/keryke/arlo-architecture-and-buildout`,
`/keryke/talaria-browser-os`, `/keryke/tabula-and-chione-lineage`,
`/keryke/crimson-desert-companion`, and `/keryke/frostbite-hq-bleed-boundary`.

### Frostbite

Question: What are Frostbite's key business operations, inventory, shipping, and
Shopify themes?

Answer from brain: Frostbite memory clusters around cold-chain and shipping model,
freezer/SKU inventory control, show operations, and the website/Shopify/catalog
surface. Cited concepts included `/frostbite/cold-chain-and-shipping-model`,
`/frostbite/inventory-freezer-and-sku-control`,
`/frostbite/show-and-booth-operations`, and
`/frostbite/website-shopify-and-catalog`.

### Lyhna

Question: What is Lyhna's witness/proof layer and how does Axlio relate?

Answer from brain: Lyhna clusters around witness/proof, governed-loop evidence,
sync brief/proof projects, and binding economics. Axlio belongs with Lyhna, not
AI-theory, as the origin/value/system-design lineage. Cited concepts included
`/lyhna/witness-and-proof-layer`, `/lyhna/loop-forge-governed-loop`,
`/lyhna/tas-sync-brief-and-proof-projects`, `/lyhna/agent-cost-and-binding-economics`,
and `/lyhna/axlio-origin-and-value`.

## Win Gate

- At least 50 concepts: pass (`73` mined, `76` total concept files after reconciliation).
- Cold-amnesia test across 3 domains: pass.
- Includes Keryke and Frostbite cold questions: pass.
- `NEEDS_DECISION` was not mined: pass.
