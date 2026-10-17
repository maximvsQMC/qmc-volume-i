#!/usr/bin/env python3
"""Validate HF release with Python stdlib (no network and no optional packages)."""
from __future__ import annotations
from collections import Counter, defaultdict
import hashlib, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent
DATA=ROOT
META=ROOT


def sha_bytes(data): return hashlib.sha256(data).hexdigest()
def sha_text(s): return sha_bytes(s.encode('utf-8'))
def load_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line]


def main():
    m=json.loads((META/'hf_manifest.json').read_text(encoding='utf-8'))
    source=ROOT/m['source_file']
    assert source.is_file()
    assert sha_bytes(source.read_bytes())==m['source_file_sha256']
    records=load_jsonl(DATA/'qmc_full_text.jsonl')
    chunks=load_jsonl(DATA/'qmc_rag_chunks.jsonl')
    assert len(records)==m['record_count']==100
    assert len(chunks)==m['chunk_count']==1282
    assert len({r['record_id'] for r in records})==100
    assert sorted(r['training_order'] for r in records)==list(range(1,101))
    assert len({r['source_sequence'] for r in records})==100
    assert sum(r['source_kind']=='Medium_essay' for r in records)==m['medium_essay_count']==99
    assert sum(r['source_kind']=='QRT_research_template' for r in records)==1
    assert sum(r['body_char_count'] for r in records)==m['total_body_char_count']
    assert sum(r['body_word_count'] for r in records)==m['total_body_word_count']
    ids={r['record_id']:r for r in records}
    for r in records:
        body=r['full_text']
        assert sha_text(body)==r['body_sha256'],r['record_id']
        assert len(body)==r['body_char_count'],r['record_id']
        assert len(body.split())==r['body_word_count'],r['record_id']
        assert len(body.splitlines())==r['body_line_count'],r['record_id']
        assert r['dataset_version']=='2.0'
    assert sha_text('\n\n'.join(r['full_text'] for r in sorted(records,key=lambda r:r['source_sequence'])))==m['concatenated_body_sha256']
    by=defaultdict(list)
    for c in chunks:
        assert sha_text(c['text'])==c['chunk_sha256'],c['chunk_id']
        assert c['record_id'] in ids
        assert c['body_sha256']==ids[c['record_id']]['body_sha256']
        assert len(c['text'])==c['end_char']-c['start_char']
        by[c['record_id']].append(c)
    for rid,r in ids.items():
        items=sorted(by[rid],key=lambda c:c['chunk_index'])
        assert items and [c['chunk_index'] for c in items]==list(range(len(items)))
        assert all(c['chunk_count']==len(items) for c in items)
        assert items[0]['start_char']==0 and items[-1]['end_char']==len(r['full_text'])
        assert ''.join(c['text'] for c in items)==r['full_text'],rid
        for i,c in enumerate(items):
            assert r['full_text'][c['start_char']:c['end_char']]==c['text']
            assert c['previous_chunk_id']==(items[i-1]['chunk_id'] if i else None)
            assert c['next_chunk_id']==(items[i+1]['chunk_id'] if i<len(items)-1 else None)
    edges=set(); seen=set()
    for r in records:
        for p in r['dependency_parents']:
            assert p in ids and p!=r['record_id']
            edges.add((p,r['record_id']))
        for ch in r['dependency_children']:
            assert ch in ids and ch!=r['record_id']
            seen.add((r['record_id'],ch))
    assert edges==seen and len(edges)==m['dependency_edge_count']==115
    edgefile=(META/'dependency_edges.tsv').read_text(encoding='utf-8').splitlines()
    assert edgefile[0]=='from\tto\trelation'
    assert set(tuple(line.split('\t'))[:2] for line in edgefile[1:])==edges
    assert all(len(line.split('\t'))==3 and line.split('\t')[2] for line in edgefile[1:])
    # Kahn DAG check.
    parents={rid:set(r['dependency_parents']) for rid,r in ids.items()}
    done=set()
    while len(done)<len(ids):
        candidates=[rid for rid,p in parents.items() if rid not in done and p.issubset(done)]
        assert candidates,'Cyclic dependency graph'
        done.update(candidates)
    dcounts=Counter(r['primary_domain_id'] for r in records)
    assert dict(sorted(dcounts.items()))==m['domain_counts']
    assert sorted(r for r in ids if int(r[-3:])>=96)==m['record_ids_added_since_v1_0']
    sha_file=ROOT/'SHA256SUMS.txt'
    if sha_file.exists():
        for line in sha_file.read_text(encoding='utf-8').splitlines():
            digest,rel=line.split('  ',1)
            path=ROOT/rel
            assert path.is_file() and sha_bytes(path.read_bytes())==digest, rel
    print('PASS: 100 original records; 1,282 exact-reconstructable chunks; 115 DAG edges; 12 domains; source SHA-256 and body hashes verified.')
    if sha_file.exists(): print('PASS: SHA256SUMS.txt verified')

if __name__=='__main__': main()
