# QMC Volume I — Version 2.0

## Corpus changes

- 100 primary research records: 99 Medium essays and one QRT research template.
- Five records added since Version 1.0: `QMC-V1-096` through `QMC-V1-100`.
- 12 primary domains and 115 curated conceptual dependency edges.
- Fourteen external QRT source records remain nested references, not additional primary articles.

## Data representations

- `qmc_full_text.jsonl`: 100 complete records with source metadata.
- `qmc_rag_chunks.jsonl`: 1,282 contiguous, nonoverlapping fragments of the same records.
- Both representations retain article IDs and provenance. They are not independent corpora.

## Export methodology

Record bodies and metadata are extracted from the canonical Version 2.0 Markdown.
Every body is checked against its source SHA-256. Fragments preserve the original
text and reconstruct each complete article exactly. Chunk boundaries favor
paragraph boundaries and intact fenced code blocks where possible.

JSONL records follow `training_order`, which is distinct from source chronology.
The conceptual dependency graph is checked for parent/child consistency and
acyclicity. No synthetic questions, answers, or factual labels were introduced.

## Scope

CC BY 4.0 applies to original author-controlled materials as described in
LICENSE.md and LICENSE_STATUS.md. Third-party rights remain separate.
Historical metadata in the canonical source is preserved.

The corpus represents an open research program. It is not a validated factual
benchmark. No model-training results, retrieval benchmark scores, or manual
correctness annotations are claimed. Identity to current live source pages
is not asserted.
