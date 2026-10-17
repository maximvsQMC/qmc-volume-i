#!/usr/bin/env python3
"""Optional local conversion of HF JSONL configurations to Parquet.
Install pyarrow first; JSONL alone is fully supported on the Hub.
"""
from pathlib import Path
import json
try:
    import pyarrow as pa
    import pyarrow.parquet as pq
except ImportError as exc:
    raise SystemExit('Optional dependency unavailable. Install pyarrow (pip install pyarrow) or let Hugging Face auto-convert the uploaded JSONL.') from exc
ROOT = Path(__file__).resolve().parent
for config in ('full_text','rag_chunks'):
    jsonl=ROOT/('qmc_full_text.jsonl' if config == 'full_text' else 'qmc_rag_chunks.jsonl')
    rows=[json.loads(s) for s in jsonl.read_text(encoding='utf-8').splitlines() if s]
    target=jsonl.with_suffix('.parquet')
    pq.write_table(pa.Table.from_pylist(rows),target,compression='zstd')
    print(f'{target}: {len(rows)} rows')
print('Add a Parquet-only YAML config if you intend to publish both physical formats; do not blindly duplicate rows in one config.')
