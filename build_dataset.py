#!/usr/bin/env python3
"""Rebuild the QMC HF JSONL exports from the canonical Volume I v2.0 Markdown.
Requires: PyYAML. Preserves every body exactly and verifies source hashes.
Usage: python build_dataset.py
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent
SOURCE_NAME = 'QMC_Volume_I_Training_Dataset_Version_2.0.md'
SOURCE = ROOT / SOURCE_NAME
DATA = ROOT
META = ROOT
RECORD_RE = re.compile(r'<!-- QMC_RECORD_START id="(QMC-V1-\d{3})" -->\n(.*?)<!-- QMC_RECORD_END id="\1" -->', re.S)
YAML_RE = re.compile(r'```yaml\n(.*?)\n```', re.S)
BODY_RE = re.compile(r'<!-- QMC_FULL_TEXT_START -->\n\n(.*?)\n\n<!-- QMC_FULL_TEXT_END -->', re.S)


def digest(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def write_jsonl(path: Path, rows) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='\n') as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(',', ':')) + '\n')


def atomic_blocks(text: str):
    """Return (start,end) spans at blank lines, keeping fenced code blocks whole."""
    pos, start, in_fence, token = 0, 0, False, ''
    ranges=[]
    for line in text.splitlines(keepends=True):
        stripped=line.strip()
        match=re.match(r'^(`{3,}|~{3,})', stripped)
        if match:
            fence=match.group(1)
            if not in_fence:
                in_fence, token = True, fence[0]
            elif stripped.startswith(token * 3):
                in_fence=False
        pos+=len(line)
        if not in_fence and not stripped:
            ranges.append((start,pos))
            start=pos
    if start < len(text):
        ranges.append((start,len(text)))
    return ranges


def split_chunks(text: str, target: int = 4200):
    atoms=atomic_blocks(text)
    parts=[]; cur_start=0; cur_end=0
    for start,end in atoms:
        if cur_end > cur_start and end-cur_start > target:
            parts.append((cur_start,cur_end))
            cur_start=start
        cur_end=end
    if cur_end > cur_start:
        parts.append((cur_start,cur_end))
    assert parts and parts[0][0]==0 and parts[-1][1]==len(text)
    assert all(a[1]==b[0] for a,b in zip(parts,parts[1:]))
    return parts


def heading_before(text: str, pos: int) -> str:
    # Only a lookup annotation; does not modify any byte of the payload.
    prefix=text[:pos]
    headings=re.findall(r'^#{1,6} +([^\n]+)',prefix,re.M)
    return headings[-1].strip() if headings else ''


def main():
    raw=SOURCE.read_text(encoding='utf-8')
    front=yaml.safe_load(raw.split('---',2)[1]); match=list(RECORD_RE.finditer(raw))
    assert len(match)==100, len(match)
    recs=[]; all_chunks=[]; seen=set(); edges=[]
    for item in match:
        rid,sect=item.group(1),item.group(2)
        ym=YAML_RE.search(sect); bm=BODY_RE.search(sect)
        assert ym and bm, f'Missing metadata or body for {rid}'
        md=yaml.safe_load(ym.group(1)); body=bm.group(1)
        assert md['record_id']==rid and rid not in seen
        seen.add(rid)
        assert digest(body)==md['body_sha256'],rid
        assert len(body)==md['body_char_count'],rid
        assert len(body.split())==md['body_word_count'],rid
        assert len(body.splitlines())==md['body_line_count'],(rid,len(body.splitlines()),md['body_line_count'])
        row={'dataset_id':'QMC-VOLUME-I','dataset_version':'2.0',**md,'full_text':body}
        recs.append(row)
        for p in md['dependency_parents']:
            edges.append((p,rid))
        for i,(start,end) in enumerate(split_chunks(body)):
            chunk=body[start:end]
            all_chunks.append({
                'chunk_id':f'{rid}-C{i+1:04d}', 'record_id':rid,
                'dataset_version':'2.0','title':md['title'],
                'author':md['author'],'source_url':md['source_url'],
                'primary_domain_id':md['primary_domain_id'],'primary_domain':md['primary_domain'],
                'source_kind':md['source_kind'],
                'training_order':md['training_order'],'source_sequence':md['source_sequence'],
                'chunk_index':i, 'start_char':start,'end_char':end,
                'section_heading':heading_before(body,start),
                'body_sha256':md['body_sha256'],'chunk_sha256':digest(chunk),
                'text':chunk,
            })
    recs.sort(key=lambda x:x['training_order'])
    chunks_by=defaultdict(list)
    for chunk in all_chunks:
        chunks_by[chunk['record_id']].append(chunk)
    for items in chunks_by.values():
        for i,chunk in enumerate(items):
            chunk['chunk_count']=len(items)
            chunk['previous_chunk_id']=items[i-1]['chunk_id'] if i else None
            chunk['next_chunk_id']=items[i+1]['chunk_id'] if i<len(items)-1 else None
    all_chunks.sort(key=lambda x:(x['training_order'],x['chunk_index']))
    assert len(recs)==front['record_count']==100
    assert len(edges)==front['dependency_edge_count']==115
    assert len(set(edges))==115
    assert sum(r['body_word_count'] for r in recs)==front['total_body_word_count']
    assert sum(r['body_char_count'] for r in recs)==front['total_body_char_count']
    assert sorted(r['training_order'] for r in recs)==list(range(1,101))
    indexed={r['record_id']:r for r in recs}
    for p,c in edges:
        assert p in indexed and c in indexed
        assert c in indexed[p]['dependency_children'],(p,c)
    for r in recs:
        assert set(r['dependency_children']) == {c for p,c in edges if p==r['record_id']},r['record_id']
    order=[r['full_text'] for r in sorted(recs,key=lambda x:x['source_sequence'])]
    assert digest('\n\n'.join(order))==front['concatenated_body_sha256']
    assert all(''.join(c['text'] for c in chunks_by[r['record_id']])==r['full_text'] for r in recs)
    write_jsonl(DATA/'qmc_full_text.jsonl',recs)
    write_jsonl(DATA/'qmc_rag_chunks.jsonl',all_chunks)
    domain=Counter(r['primary_domain_id'] for r in recs)
    (META/'domain_counts.json').write_text(json.dumps(dict(sorted(domain.items())),indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    graph=re.search(r'### Machine-readable dependency edge list\s+```tsv\n(.*?)\n```',raw,re.S)
    assert graph, 'Machine-readable edge list not found'
    graph_lines=graph.group(1).splitlines()
    assert graph_lines[0]=='from\tto\trelation'
    graph_edges=[tuple(line.split('\t')) for line in graph_lines[1:] if line.strip()]
    assert len(graph_edges)==115 and {(p,c) for p,c,_ in graph_edges}==set(edges)
    (META/'dependency_edges.tsv').write_text('\n'.join(graph_lines)+'\n',encoding='utf-8')
    manifest={
        'format':'qmc-huggingface-dataset/1.0','dataset_id':'QMC-VOLUME-I',
        'dataset_version':'2.0','source_file':SOURCE_NAME,
        'source_file_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'record_count':len(recs),'chunk_count':len(all_chunks),
        'medium_essay_count':sum(r['source_kind']=='Medium_essay' for r in recs),
        'qrt_primary_record_count':sum(r['source_kind']!='Medium_essay' for r in recs),
        'nested_qrt_source_records_referenced_not_duplicated':14,
        'domain_counts':dict(sorted(domain.items())),
        'dependency_edge_count':len(edges),
        'total_body_word_count':sum(r['body_word_count'] for r in recs),
        'total_body_char_count':sum(r['body_char_count'] for r in recs),
        'concatenated_body_sha256':front['concatenated_body_sha256'],
        'reading_order':'training_order ascending, not source chronology',
        'language_note':'primary source text predominantly English; no passage-level language labels',
        'copyright_note':'Author-selected CC BY 4.0 for original author-controlled materials distributed in this HF release; third-party rights remain separate. Canonical source snapshot historical metadata preserved.',
        'hf_configs':{'full_text':'qmc_full_text.jsonl','rag_chunks':'qmc_rag_chunks.jsonl'},
        'splits_note':'train is the only storage split, not an independently curated model training benchmark',
        'record_ids_added_since_v1_0':[f'QMC-V1-{i:03d}' for i in range(96,101)],
        'license':'cc-by-4.0',
        'huggingface_dataset_url':'https://huggingface.co/datasets/MaximvsQMC/qmc-volume-i',
        'hf_repository_layout':'browser_upload_flat_root_unique_data_filenames',
    }
    (META/'hf_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f"Generated {len(recs)} full-text records, {len(all_chunks)} losslessly reconnectable chunks; verified {len(edges)} dependency edges")

if __name__=='__main__':
    main()
