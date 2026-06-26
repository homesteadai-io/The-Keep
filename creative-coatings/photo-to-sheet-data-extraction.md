---
type: Concept
title: Photo-to-sheet data extraction
description: Photos need to become structured sheet rows with customer, part, paint color, quantity, and tool fields.
domain: creative-coatings
status: canonical
confidence: high
source_refs: [/_raw/creative-coatings/claude-corpus-2026-06-25/photo-to-sheet-data-extraction-evidence.json]
tags: [creative-coatings, claude-corpus, phase-2-mine, explored-rejected]
created: 2026-06-25T00:00:00Z
updated: 2026-06-25T00:00:00Z
---

# Photo-to-sheet data extraction

## Verdict

Photos need to become structured sheet rows with customer, part, paint color, quantity, and tool fields.

## Durability

- Reconciled source count: 61
- Confidence: high
- Repetition is treated as signal; this concept collapsed repeated chat/doc evidence into one file.

## Evidence

- `chat:d09f7204-4d3d-4329-b16a-202118367bba` (chat, 56 msgs): Project digest requirements — lo's voice (ElevenLabs Callum) speaking identification results aloud, a scheduling layer that captures holding inventory and generates optimized run orders based on Adam's parameters (color grouping, tooling, part size, quantity, due date priority), and a mobile PWA interface requiring no app install. A complete build specification was created and saved, covering 17 sections including reference library schema, onboarding app design, vision engine selection rationale, scheduling parameters, ha...
- `chat:e9903c13-1a3a-438f-a0ed-fe6694582f50` (chat, 56 msgs): google drive file system, Cowork — work's Project model limitation (project location is grayed out and cannot be edited post-creation, requiring a new project if the scope needs to change). Adam provided per-file routing corrections: Mercury is an active customer (route to existing Mercury Prod. Quoted Dwgs/ folder), Patrick is a retired customer (Archive), Gema files should be deleted, and traveler HEIC photos belong in Projects/Vision-Barcode-App/Reference-Photos/ as vision system reference material. The run completed with 1...
- `chat:f511017d-680e-49c7-958a-4596b1adb9b6` (chat, 50 msgs): Plateshop database format analysis and integration planning — , truncates and reloads eight tables into a four-schema Supabase contract (`mirror.*`, `ref.*`, `live.*`, `ops.*`), and idempotency was proven with two identical loads producing identical counts (capture_events 120,629, customers 221, lots 165,709, containers 79,051, delivery_tickets 41,416) and two distinct receipts in `ops.mirror_load_log`. A loader defect (delivery_tickets PK mapped to `ID` instead of `DeliveryTicketID`) was caught and fixed during the first real load; the fix currently ex...
- `chat:943d7fa6-8954-4a73-b88e-4dde20019db2` (chat, 40 msgs): Claude Chrome scheduler — and work-in-process visibility across the company. In the traveler workstream, Adam uploaded a zip file of 31 HEIC photos from a Google Drive folder. Claude converted them to JPEG, read each one, extracted part number, customer, quantity, color, due date, and work order fields, deduplicated 31 photos into 21 unique travelers (using Part # + WO # as the composite key), and produced a formatted Excel workbook with a data table, flagged rows, and a Read Notes audit sheet. Key findings included t...
- `chat:4a3aeaf1-8040-4420-9cc6-b1707e063d05` (chat, 40 msgs): Daily powder line schedule automation system — the system: a two-tab Google Sheet with a Master Capture tab (every traveler field, every part, every day — the permanent analytic asset driving future company intelligence) and a Floor Schedule tab (four fields only — Customer, Part Number, Quantity, Paint Color — derived from Master and printed for the floor crew). The key design principle locked throughout was "capture everything faithfully, interpret nothing in v1" — Plateshop's inconsistent tooling and density notation is a known upstrea...
- `chat:2adb82b5-253e-4f0b-b6fe-c466a36757c1` (chat, 35 msgs): quote creative coatings — (legacy placeholder) and 12-person crew (varies), operating Tuesday-Friday on 4×10 hour shifts. The conversation revealed that actual throughput calculations require five variables: tooling width, inter-rack gap, crate quantity, pieces per rack, and next crate/new part separator gap (192 inches). Using the Grede quote as an example, the corrected formula showed actual throughput of 514 pcs/hr versus the quoted 1,620 pcs/hr, transforming what appeared to be a profitable part into one losing ap...
- `chat:67c91c24-306a-4fd6-95b9-a8517aea64fb` (chat, 30 msgs): Higgsfield review — t now: - **Gmail, Google Calendar, Google Drive** — Claude can read, search, draft, schedule directly. You don't need to open Gmail to send most messages. - **Shopify** — full admin access. Inventory, orders, products, customers, analytics. The Frostbite store is operable from chat. - **Calendly** — scheduling, link creation, invitee management. - **Supabase** — database ops directly. - **Tripadvisor** — travel. - **Clay** — contact and company research. - **PitchBook** — investment research....
- `chat:aed8c14d-d7c5-494e-8949-e66bd80d7119` (chat, 25 msgs): Powder line operation quote areas — r gap)) × Crate qty, where Effective pitch = Tooling width + Inter-rack gap. Adam standardized the output format as a three-column Excel workbook titled "Quote Audit" with the naming convention Quote_Audit_[PartNumber]_[Customer].xlsx. The three columns are: "What the Quote Says," "What It Actually Costs," and "Difference." Rows are preserved from the detailed version (line constants, part-level inputs, throughput calculation, cost per piece, margin, and root cause sections), with a Formula D...

## Explored / Rejected Signals

- `chat:0bc0f65b-7cfd-4b1d-9aff-3a2b7057267a`
- `chat:128a9150-6fe7-40b8-9911-9f308e574086`
- `chat:2adb82b5-253e-4f0b-b6fe-c466a36757c1`
- `chat:30d25697-579c-4dc5-bdc9-73572f1c7254`
- `chat:3da780d8-d8bf-4f97-89e1-7d7ca2077abc`
- `chat:3dbebae5-b353-494b-b135-99ffd208a4c9`
- `chat:3e244879-19e6-4cf6-93dc-9a5d8a76928a`
- `chat:43603d30-75e0-47ec-8403-3d6ca19c45ba`
- `chat:4a3aeaf1-8040-4420-9cc6-b1707e063d05`
- `chat:62e0c6ea-f8fc-40d8-936c-ecedbae8306a`
- `chat:67c91c24-306a-4fd6-95b9-a8517aea64fb`
- `chat:76f5fc4e-202b-4341-8fb5-36c38adefd86`

## Contradictions / Open Questions

- None flagged in this pass.

## Source Trail

- Redacted evidence bundle: [/_raw/creative-coatings/claude-corpus-2026-06-25/photo-to-sheet-data-extraction-evidence.json](/_raw/creative-coatings/claude-corpus-2026-06-25/photo-to-sheet-data-extraction-evidence.json)
- Source export: `Anthropic Claude Chat Corpus .zip`
