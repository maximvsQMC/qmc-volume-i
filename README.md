# Quantum Metaphysics of Connectedness — Volume I Training Dataset (v2.0)

**Author and research-program originator:** Maximvs Shlygin  
**Corpus period:** 2025–2026  
**Version:** 2.0 · **Primary records:** 100 · **Medium essays:** 99 · **QRT primary records:** 1  
**Canonical entry point:** `QMC-V1-067` — *The Asthma of Reality’s Paradoxes*  
**Previous published dataset record:** [Zenodo 23145624, Version 1.0](https://zenodo.org/records/23145624)  
**Hugging Face repository:** [MaximvsQMC/qmc-volume-i](https://huggingface.co/datasets/MaximvsQMC/qmc-volume-i). The Zenodo link above identifies Version 1.0, not this Version 2.0 dataset.

> **License:** The author has selected **Creative Commons Attribution 4.0 International (CC BY 4.0)** for the original author-controlled dataset materials distributed in this dataset. Attribute Maximvs Shlygin and retain source provenance. Third-party quoted material, external publications, and linked resources may carry separate rights; this license does not override them. See [LICENSE.md](LICENSE.md) and [License and rights notes](LICENSE_STATUS.md). Earlier frozen archival source metadata stating `not_specified_in_source_materials` reflects its original preparation and has not been silently rewritten.

## Dataset summary

This repository provides a **machine-readable, provenance-preserving representation of 100 full research records** from *Quantum Metaphysics of Connectedness (QMC)*, an **open research program based on the QMC method**. The corpus contains essays spanning methodological and conceptual questions, cosmology and quantum physics, mathematics, biology, AI, social systems, economics, and ecology. It is intended for long-document search, retrieval-augmented generation (RAG), conceptual graph exploration, corpus studies, and testing AI systems' ability to distinguish **established science, QMC-internal reasoning, hypotheses, and metaphors**.

**QMC is not represented as a completed empirical theory, a substitute for scientific proof, or a uniform source of validated scientific facts.** Its methodology uses concepts such as invariant `Z`, comparison `~`, unfolding `==>`, retained difference, and time-dependent viability checks. A proposed correspondence is **not** an identity or a proof of causation.

The canonical body of every record has been preserved **exactly** from the Version 2.0 Markdown training dataset: no summarization, correction, title rewriting, or removal of formulas and ASCII schemes was applied to the `full_text` field. SHA-256 payload hashes verify the preservation.

## The QMC method

Quantum Metaphysics of Connectedness is an open research program that uses the QMC method to examine paradoxes and relationships across domains. In the methodological entry point, the author presents it as a way to identify where descriptions conflict, recover a workable framing, and identify the next appropriate tool: mathematical proof, empirical investigation, practical design, or an explicit limit.

The method uses `L` for viable connectedness, `Z` for an invariant across descriptions, `~` for correspondence, and `==>` for unfolding between levels or contexts. The temporal sequence `L ==> L ==> L` asks whether connectedness can continue through a change. These are terms of the research program; a correspondence between domains does not establish physical identity or causation.

Volume I brings together methodological foundations and applications across physical, living, cognitive, and social systems. Reading the collection as a whole makes it possible to examine how this common vocabulary is used, where its interpretations differ, and how conceptual dependencies connect individual studies.

## Volume I at a glance

Version 2.0 is a complete, self-contained edition: **100 primary records**, including **99 Medium essays and one QRT research template**, with **752,209 body words**. It includes the earlier 95 records as well as five additions; no Version 1.0 download is needed to read this volume.

The corpus spans the following 12 primary domains. Descriptions summarize the subjects represented in each group; they do not imply that the claims have been independently validated.

| Domain | Primary field | Records | Subjects covered |
|---|---|---:|---|
| D01 | Method, Core Ontology & Epistemology | 6 | The QMC method, truth, intuition, information, and relations between descriptions. |
| D02 | Connectedness, Love, Family & Continuation | 15 | Harmony, love, family, hope, self-preservation, and the continuation of connectedness. |
| D03 | Cosmology, Space, Time & Cosmic Evolution | 12 | Space, time, cosmic evolution, hydrogen, light, and the Fermi paradox. |
| D04 | Black Holes, Horizons & Gravitational Information | 4 | Black holes, horizons, firewalls, and gravitational information. |
| D05 | Quantum Physics, Information & Computation | 8 | Teleportation, cryptography, coherence, quantum computing, particle distinctions, and transparency. |
| D06 | Mathematics & Formal Proof Architecture | 3 | The golden ratio, pi, and the Quantum Rigidity Template (QRT). |
| D07 | Biology, Medicine & Living Systems | 14 | Living systems, evolution, immunity, cancer, aging, memory, and the origin of life. |
| D08 | Mind, Self, Consciousness & Meaning | 12 | Consciousness, identity, freedom, guilt, happiness, sleep, and meaning. |
| D09 | AI, Machine Agency & Digital Systems | 6 | AI representation, perception, agency, conscience, and the QMC protocol for AI. |
| D10 | Society, Power, Civilization, Culture & Art | 12 | Power, collective life, civilization, governance, culture, poetry, and music. |
| D11 | Economics, Strategy, Risk & Games | 6 | Profit, success, risk, strategy, markets, backgammon, and chess. |
| D12 | Earth Systems, Ecology & Planetary Futures | 2 | Planetary futures, Earth systems, and the Gulf Stream. |

**[Browse all 100 works in the complete catalogue](CATALOG.md).** Each entry provides its stable record ID, original title, source link, and reading-order position.

## Where to begin

1. Start with **QMC-V1-067 — The Asthma of Reality’s Paradoxes**, the corpus’s canonical methodological entry point.
2. Continue through the six records in **D01: Method, Core Ontology & Epistemology**, in the order shown in the catalogue. These introduce the vocabulary used throughout the volume.
3. Choose a domain of interest from the table above. Read the complete articles in the canonical Markdown or in `qmc_full_text.jsonl`.
4. Follow each record’s `dependency_parents` for conceptual prerequisites and `dependency_children` for related developments. Use source links when citing individual works.

The provided `training_order` is a methodological reading route, not publication chronology or a requirement to read every preceding article. The full catalogue follows this order within each domain.

## How the studies connect

The corpus includes **115 directed conceptual dependency edges** linking the 100 records. In `dependency_edges.tsv`, an edge runs from a conceptual prerequisite (`from`) to a dependent record (`to`); `relation` describes the connection. The JSONL metadata also stores reciprocal parent and child lists.

For example, the methodological entry point `QMC-V1-067` is a recorded parent of **IT IS BIT** (`QMC-V1-078`), **PROTOCOL L FOR AI** (`QMC-V1-080`), and the **Quantum Rigidity Template** (`QMC-V1-091`). These links offer routes from the shared method into information, AI, and mathematics. They are curated conceptual relationships, not evidence that one article proves another’s claims.

## What readers can do with this dataset

- **Read and compare:** explore complete articles across domains while retaining their original text and attribution.
- **Search and retrieve:** index 1,282 text fragments, trace results to the original record, and reconstruct each article exactly.
- **Explore conceptual structure:** inspect the domain groupings and prerequisite graph to follow connections across the research program.
- **Study the corpus computationally:** analyze terminology, cross-references, and reasoning patterns with stable IDs and verifiable text hashes.

## Quick start

Download and extract this repository, then run:

```bash
python validate_dataset.py
```

Validation uses only the Python standard library. To rebuild exports:

```bash
python -m pip install -r requirements.txt
python build_dataset.py
python validate_dataset.py
```

Read locally without third-party packages:

```python
import json
from pathlib import Path

with Path("qmc_full_text.jsonl").open(encoding="utf-8") as stream:
    records = [json.loads(line) for line in stream if line.strip()]
print(len(records), records[0]["record_id"])
```

## File layout

| File | Contents |
|---|---|
| `QMC_Volume_I_Training_Dataset_Version_2.0.md` | Canonical corpus: full articles and source metadata. |
| `CATALOG.md` | Complete index of all 100 works, grouped by domain with reading order and source links. |
| `qmc_full_text.jsonl` | 100 complete research records, one JSON object per line. |
| `qmc_rag_chunks.jsonl` | 1,282 contiguous text fragments with record IDs and character offsets. |
| `dependency_edges.tsv` | 115 conceptual dependency edges. |
| `domain_counts.json` | Record counts across 12 primary domains. |
| `hf_manifest.json` | Export metadata, corpus statistics, and source hashes. |
| `build_dataset.py` | Reproduce JSONL exports from the canonical Markdown. |
| `validate_dataset.py` | Verify text integrity, chunk reconstruction, graph, and file checksums. |
| `export_parquet_optional.py` | Optional conversion from JSONL to Parquet; requires `pyarrow`. |
| `requirements.txt` | Dependency for rebuilding the dataset. |
| `SHA256SUMS.txt` | SHA-256 checksums for all other distributed files. |
| `LICENSE.md`, `LICENSE_STATUS.md` | License and scope of rights. |
| `RELEASE_NOTES.md` | Version 2.0 changes and export methodology. |

## Configurations and splits

The dataset provides **two alternative *representations*** of the same underlying 100 studies; they must **not** be counted as 1,382 independent original research works.

| Configuration | Split | Rows | Unit | Recommended use |
|---|---|---:|---|---|
| `full_text` (default) | `train` | **100** | Complete source essay | Citation-grounded reading, structured analysis, graph tasks. |
| `rag_chunks` | `train` | **1,282** | Lossless contiguous text span of an essay | Semantic indexing, RAG, long-document retrieval. |

The name `train` here means **one storage split**, *not* a scientifically constructed training/validation/test partition or a benchmark. Do not report evaluation accuracy based on random splits of strongly cross-referencing studies without controlling document and concept overlap.

Every `rag_chunks` record has `record_id`, `chunk_index`, `start_char`, `end_char`, `chunk_sha256`, and the full record's `body_sha256`. Concatenating the chunks of a record in `chunk_index` order yields the **exact original** `full_text` value. The chunk boundaries favor blank lines and intact fenced code blocks. Chunks are **not** human semantic annotations and may exceed the target size for exceptionally long individual blocks.

## How to load

To load the Hugging Face distribution with the optional `datasets` package:

```python
from datasets import load_dataset

full = load_dataset("MaximvsQMC/qmc-volume-i", "full_text", split="train")
chunks = load_dataset("MaximvsQMC/qmc-volume-i", "rag_chunks", split="train")

assert len(full) == 100
assert len(chunks) == 1282
print(full[0]["record_id"], full[0]["title"])
print(chunks[0]["record_id"], chunks[0]["chunk_index"])
```

**No custom dataset loader or remote code execution is required.** The Hugging Face distribution exposes separate `full_text` and `rag_chunks` configurations. HF Dataset Viewer may generate convenient Parquet exports from these JSONL configurations. This package also includes an optional local Parquet export script (requires `pyarrow`).

For offline use, `datasets.load_dataset("json", data_files="qmc_full_text.jsonl", split="train")` also works when `datasets` is installed.

## Data fields

`full_text` contains the entire authorial text, and all source metadata fields are retained from the canonical corpus wrapper, including:

- IDs and ordering: `record_id`, `source_sequence`, `training_order`, `dataset_version`.
- Authorship and publication: `title`, `author`, `source_kind`, `source_url`, `medium_id`, `source_date`, URL and extraction status.
- Editorial grouping: `primary_domain_id`, `primary_domain`, `domain_tags`.
- Graph links: `dependency_parents`, `dependency_children`, `explicit_title_crossrefs`.
- Text-preservation metadata: `text_diagrams_preserved`, `text_formulas_preserved`, `tables_preserved_as_text`, `body_char_count`, `body_word_count`, `body_line_count`, `body_sha256`.
- Text: `full_text` (not rewritten, redacted, normalized, or synthesized).

A **dependency edge** represents a curated conceptual prerequisite, **not** external scientific proof. A record's primary domain is an editorial grouping, not a claim it belongs exclusively to that discipline. `source_sequence` preserves inherited corpus provenance and is **not** publication chronology. `training_order` indicates a methodological reading route, **not** a label describing model suitability.

A separate `dependency_edges.tsv` and `domain_counts.json` aid graph exploration. `hf_manifest.json` describes the transform and verification values.

## Provenance, extraction and limitations

- `QMC_Volume_I_Training_Dataset_Version_2.0.md` is the **normative canonical full-text Markdown input** for this dataset; `qmc_full_text.jsonl` is its record-wise view.
- An author-supplied English Markdown file supplied the content of `QMC-V1-100` in the canonical source, and its Medium URL documents its published source. Exact identity to the current public Medium HTML text is **not asserted**.
- Some earlier sources were obtained through web or PDF extraction; source-specific preservation indicators are in each record. This export does not regenerate missing image-only content.
- Language is predominantly English. This export does not perform passage-level language tagging, scientific verification, claim checking, PII filtering, or automated evidence classification.
- The nested 14 QRT external research sources are cited/referenced in the canonical corpus, **not** duplicated as full-text records.
- Source publication is **not** independent verification of mathematical proofs, biomedical advice, or QMC hypotheses.

**Training considerations:** This is long-form, non-instruction-tuned text with potentially philosophical, speculative, contested, or provisional assertions. It is **not** a curated fact-only corpus. Model developers should preserve article-level attribution, maintain explicit distinctions among scientific claims and speculative interpretations, implement appropriate evaluation and data governance, and follow applicable content rights.

## Integrity and reproducibility

The provided exports were checked against every source `body_sha256`, the canonical concatenated-body SHA-256, row counts, graph reciprocity, and round-trip reconstruction of all chunk texts. The SHA-256 file covers repository artifacts, excluding the checksum file itself.

Rebuild or validate locally:

```bash
python build_dataset.py    # requires PyYAML
python validate_dataset.py # Python standard library only
```

See `hf_manifest.json`, `dependency_edges.tsv`, and `SHA256SUMS.txt`.

## Changes since published Version 1.0

The prior dataset contained **95 primary records** (94 Medium essays and one QRT primary record). Version 2.0 contains **100** (99 Medium essays and one QRT). Five records were added, with their stable IDs:

| Record | Primary work | New line of inquiry |
|---|---|---|
| `QMC-V1-096` | [The Indifference Paradox](https://medium.com/@shlygin_61632/quantum-metaphysics-of-connectedness-the-indifference-paradox-3904fe470bad) | Addressability, indifference, persistence of connectedness. |
| `QMC-V1-097` | [The Paradox of the Pauli Principle](https://medium.com/@shlygin_61632/quantum-metaphysics-of-connectedness-the-paradox-of-the-pauli-principle-6d8f6dada116) | Quantum-state admissibility and coexistence. |
| `QMC-V1-098` | [The First Generation Paradox](https://medium.com/@shlygin_61632/quantum-metaphysics-of-connectedness-the-first-generation-paradox-e3e0d7986143) | Fermion generations and material distinctions. |
| `QMC-V1-099` | [The Boson Paradox](https://medium.com/@shlygin_61632/quantum-metaphysics-of-connectedness-the-boson-paradox-97b9391dec65) | Collective modes and bosonic interactions. |
| `QMC-V1-100` | [The Transparency Paradox](https://medium.com/@shlygin_61632/quantum-metaphysics-of-connectedness-the-transparency-paradox-5e723d203ca5) | Molecular water, optical transparency, chirality, chemical continuation, and cosmic comparison. |

The 95 Version 1.0 records retain their source payloads. **14 QRT-related external mathematical Zenodo source records remain nested references, not 14 additional QMC primary essays.** Version 2.0 has **12 primary domains** and **115 curated conceptual dependency edges** (79 in Version 1.0).

## Responsible use and citation

Attribution should include **Maximvs Shlygin**, *Quantum Metaphysics of Connectedness — Volume I Training Dataset (Version 2.0)*, the canonical record ID and `source_url` of the essay cited, and the eventual deposited dataset version / DOI when available. Do **not** cite the prior Version 1.0 DOI as though it identified Version 2.0.

The purpose of the dataset is to allow reproducible examination of this open research program, not to elevate every included hypothesis to an established scientific statement.
