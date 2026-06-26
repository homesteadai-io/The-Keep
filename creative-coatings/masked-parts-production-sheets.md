---
type: Concept
title: Masked parts production sheets
description: Daily masked-parts worksheets need consistent formatting, summary rows, and usable production views.
domain: creative-coatings
status: canonical
confidence: high
source_refs: [/_raw/creative-coatings/claude-corpus-2026-06-25/masked-parts-production-sheets-evidence.json]
tags: [creative-coatings, claude-corpus, phase-2-mine, explored-rejected]
created: 2026-06-25T00:00:00Z
updated: 2026-06-25T00:00:00Z
---

# Masked parts production sheets

## Verdict

Daily masked-parts worksheets need consistent formatting, summary rows, and usable production views.

## Durability

- Reconciled source count: 36
- Confidence: high
- Repetition is treated as signal; this concept collapsed repeated chat/doc evidence into one file.

## Evidence

- `chat:d09f7204-4d3d-4329-b16a-202118367bba` (chat, 56 msgs): Project digest requirements — the fields that matter for this tool: | PlateShopPro Field | What It Gives You | |---|---| | Part Number | Primary identifier (TAZ7284, 311325, 78630691, 23540154-P) | | Customer | Mercury Products Corp., Winamac Coil Spring, Metal Technologies, T&W Stamping | | Part Description | "BRKT STATIC FILL (EC/P)", "FINGER CAM END OUTBOARD", "BRACKET HOOD PIVOT LH (EC/P)" | | Base Process / Quote Process | Ecoat & Powder Coat, Powder Coat, Ecoat/Mask/Powder Coat — this is your process routing | | Pro...
- `chat:e9903c13-1a3a-438f-a0ed-fe6694582f50` (chat, 56 msgs): google drive file system, Cowork — ral correction before you give the green light. ## The structural correction first **Cowork's default of "all 2018–2025 quotes → Archive/[year]/" is doctrine-correct but operationally wrong for your business.** Quote worksheets aren't archive material in the normal sense. When a customer comes back with the same part next year, you pull last year's quote to match logic, pricing, masking specs, processing time. That's reference material, not historical record. Burying eight years of quote work...
- `chat:f511017d-680e-49c7-958a-4596b1adb9b6` (chat, 50 msgs): Plateshop database format analysis and integration planning — th questions with the gaps and next steps locked in. I'm drilling into the color data more carefully — tblParts.Color is nearly empty (just 2 "Black" entries out of 4308 parts), and while PowderColor exists in the quote worksheets, that's only 559 parts and it's quote-stage, not authoritative. The real color truth lives in the traveler data tied to each job run, which is why Adam's powder schedule OCR approach makes sense — color-per-part as a stable attribute doesn't actually exist in Plates...
- `chat:943d7fa6-8954-4a73-b88e-4dde20019db2` (chat, 40 msgs): Claude Chrome scheduler — photos from a Google Drive folder. Claude converted them to JPEG, read each one, extracted part number, customer, quantity, color, due date, and work order fields, deduplicated 31 photos into 21 unique travelers (using Part # + WO # as the composite key), and produced a formatted Excel workbook with a data table, flagged rows, and a Read Notes audit sheet. Key findings included that color (typically YN1117) was embedded in free-text instruction paragraphs rather than isolated fields, and one...
- `chat:4a3aeaf1-8040-4420-9cc6-b1707e063d05` (chat, 40 msgs): Daily powder line schedule automation system — et with a Master Capture tab (every traveler field, every part, every day — the permanent analytic asset driving future company intelligence) and a Floor Schedule tab (four fields only — Customer, Part Number, Quantity, Paint Color — derived from Master and printed for the floor crew). The key design principle locked throughout was "capture everything faithfully, interpret nothing in v1" — Plateshop's inconsistent tooling and density notation is a known upstream data-entry problem being solve...
- `chat:ef003c0a-bb14-49fe-b15c-dab53c397ff3` (chat, 24 msgs): Adding daily reviews to master revenue document — 0). Daily sheets are appended as new tabs at the bottom of the workbook. The masked-parts master uses a different template: Aptos Narrow 11pt throughout, data starting at column B row 3, with header at B2:D2 (Customer | Part # | Part Quantity), daily total formula two rows below last data row, and weekly totals placed on the last day's tab of a complete work week. A formula error was identified in four pre-existing masked-parts tabs (3.9, 3.10, 3.17, 3.18) where daily totals were inflated 2×...
- `chat:bb880c44-2a5e-45fe-8dcb-4f87e418f0d1` (chat, 18 msgs): Plateshop mirror handoff and stack status — Now I'm going to systematically examine all 15 Excel files to map out their structure—sheet names, dimensions, headers, and any formulas—while being careful not to assume consistent layouts given the known issues with masked parts and schema variations across revenue tabs. For files with many sheets like the daily revenue file with 106 tabs, I'll focus on listing sheet names and dimensions, then dive deeper into the key reference files like Part Master Powder, Tooling, the data dictionary, Ac...
- `chat:3da780d8-d8bf-4f97-89e1-7d7ca2077abc` (chat, 17 msgs): Shop activity report organization by process and department — he pipeline built across this session has four confirmed stages: (1) strict-filter artifact rows and sort master data by Process › Dept Checkout › Date in operational order (not alphabetical); (2) split into per-process worksheets after a Summary tab; (3) build a Powder Schedule isolating dual-coat and powder-only items not yet checked out of the Powder Coat department, split by feeder department in FIFO order; (4) re-run the full pipeline on a new date-range export. A fifth stage was discuss...

## Explored / Rejected Signals

- `chat:0bc0f65b-7cfd-4b1d-9aff-3a2b7057267a`
- `chat:30d25697-579c-4dc5-bdc9-73572f1c7254`
- `chat:376fc30a-bd25-41c6-a203-d347a7791b6a`
- `chat:3da780d8-d8bf-4f97-89e1-7d7ca2077abc`
- `chat:3dbebae5-b353-494b-b135-99ffd208a4c9`
- `chat:3e244879-19e6-4cf6-93dc-9a5d8a76928a`
- `chat:4a3aeaf1-8040-4420-9cc6-b1707e063d05`
- `chat:8a99cf4f-099e-4edb-af77-532387fd1f1d`
- `chat:943d7fa6-8954-4a73-b88e-4dde20019db2`
- `chat:bb880c44-2a5e-45fe-8dcb-4f87e418f0d1`
- `chat:ce5735c6-b897-4269-b2fa-a6545998a43e`
- `chat:d09f7204-4d3d-4329-b16a-202118367bba`

## Contradictions / Open Questions

- None flagged in this pass.

## Source Trail

- Redacted evidence bundle: [/_raw/creative-coatings/claude-corpus-2026-06-25/masked-parts-production-sheets-evidence.json](/_raw/creative-coatings/claude-corpus-2026-06-25/masked-parts-production-sheets-evidence.json)
- Source export: `Anthropic Claude Chat Corpus .zip`
