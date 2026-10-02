# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

The TDWG MIDS Task Group repository (Minimum Information about a Digital Specimen). It is primarily a **content/data repository for a standard**, not an application: there is no build system, package manager, linter, or test suite. Work here is mostly editing TSV/CSV term data, SSSOM mapping files, and Markdown page content.

## How the pieces fit together

- **`source/`** holds the authoritative content. It mirrors the layout of the Latimer Core repo (github.com/tdwg/ltc) and other TDWG standards.
  - `source/terms/*.tsv` — the normative data of the standard: `levels.tsv` (MIDS0–MIDS3), `information_elements.tsv` (elements with definition/purpose/usage), `discipline_terms.tsv` (Biology, Geology, Paleontology), `schemas.tsv` (discipline × element × level matrix, with an `identifier` like `Biology_CollectingAgent_MIDS2`), and `examples.tsv` (keyed by `informationElement_localName`). These files reference each other by element local name (e.g. `PhysicalSpecimenID`) and level name (e.g. `MIDS2`), so renaming an element or label must be applied consistently across all of them (and the mappings).
  - `source/mappings/*.sssom.tsv` + matching `*.sssom.yml` — SSSOM mappings from MIDS elements to target standards, one pair per `mids_<format>_<discipline>_<version>` (formats: `dwc-a`, `dwc-dp`, `abcd2`). The `.yml` holds the mapping-set metadata and `curie_map`; the `.tsv` holds one row per mapping using `sssom:`-prefixed column headers. These are consumed by the MIDS Calculator (an external R Shiny app) to compute MIDS scores, so column semantics such as `sssom:object_match_field` and `semapv:RegexRemoval` (values treated as missing) are functional, not just descriptive. `source/md/sssom-reference.md` documents the conventions. `mappings/archive/` is superseded.
  - `source/md/*.md` — page content for the documentation website. `source/resources/tools.yml` and `glossary.yml` feed the Resources page.
- **`docs/`** is the **generated** GitHub Pages site (served at mids.tdwg.org, see `docs/CNAME`). It is produced externally by **StaDocGen** (github.com/ben-norton/stadocgen, `mids` instance): source files are copied into StaDocGen, the site is built there, and the output is copied back into `docs/`. Don't hand-edit `docs/` to change content — change `source/` and note that a StaDocGen rebuild is needed. `source/stadocgen-file-map.md` lists source→StaDocGen target paths (it still references older `.csv` filenames; the term files are now `.tsv`).
- **`test/`** is scratch/experimental work rather than tests:
  - `test/_gen_terms_csv.py` — one-off generator that turns StaDocGen TSV output (`test/stadocgen/20260430/output/`) into `test/mids.csv`, an rs.tdwg.org-style term list shaped after `test/examples/latimer.csv` plus MIDS extra columns (`purpose`, `isRequiredBy`). `test/mids-column-mappings.csv` is the companion column→RDF predicate mapping. Run with `python test/_gen_terms_csv.py` (stdlib only).
  - `test/sssom-iri-test/`, `test/measurementorfact_sssom_test/` — trial variants of mapping files (e.g. resolvable MIDS IRIs, MeasurementOrFact mappings).
- **`archive/`** — retired material (charter PDF, an abandoned RDF/ontology serialization). Not maintained.

## Conventions and gotchas

- The `mids:` namespace is not yet settled: production mappings use `https://www.tdwg.org/community/cd/mids/`, while the rs.tdwg.org CSV work uses `http://rs.tdwg.org/mids/` (and lowerCamelCase local names, e.g. `physicalSpecimenID`, versus UpperCamelCase in `source/terms`). Check which context you are in before changing IRIs or casing.
- TSV files are tab-delimited with multi-value cells separated by `|` (e.g. multiple ORCID `author_id`s). Preserve tabs, header order, and encoding (UTF-8) when editing; don't let editors convert to CSV or reflow quoted text.
- `source/md/public_review/` contains public review participation docs (compact and detailed variants) for the MIDS TDWG public review; `ltc_public_review_landing_page.md` is the earlier Latimer Core equivalent kept as a reference model. Placeholders like `[START DATE]` are intentional until dates are set.
- Element definitions are discussed in GitHub issues labelled "MIDS Element" (with MIDS-0…MIDS-3 level labels) on tdwg/mids; changes to element wording generally trace back to those issues.
