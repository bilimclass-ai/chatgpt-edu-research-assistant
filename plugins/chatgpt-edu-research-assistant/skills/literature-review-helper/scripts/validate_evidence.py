#!/usr/bin/env python3
"""Offline consistency checks; does not verify source truth or replace scholarly review."""
import argparse
import collections
import datetime
import json
import re
import sys
import unicodedata

def normalized_text(text):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', str(text))).strip()

def normalized_doi(value):
    s = str(value or '').strip().lower()
    return re.sub(r'^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)', '', s)

def valid_date(value):
    try:
        datetime.date.fromisoformat(value)
        return True
    except (TypeError, ValueError):
        return False

def validate(bundle):
    errors, warnings = [], []
    def err(message): errors.append(message)
    if not isinstance(bundle, dict):
        return {'ok': False, 'errors': ['Bundle must be an object'], 'warnings': [], 'counts': {}}
    m = bundle.get('manifest', {})
    records = bundle.get('records', [])
    if not isinstance(m, dict) or not isinstance(records, list):
        return {'ok': False, 'errors': ['manifest must be an object and records a list'], 'warnings': [], 'counts': {}}
    for field in ('skill_version','search_date','question','minimum_core','required_indexes','quotes_required','reported_core'):
        if field not in m: err('manifest missing '+field)
    if m.get('skill_version') != '2.0.1': err('Unexpected skill version')
    if not valid_date(m.get('search_date')): err('Invalid manifest search date')
    if not m.get('question'): err('Missing research question')
    for field in ('minimum_core','reported_core'):
        if type(m.get(field)) is not int or m[field] < 0: err(field+' must be a nonnegative integer')
    if not isinstance(m.get('required_indexes', []), list): err('required_indexes must be a list')
    if m.get('quotes_required') not in ('all_core','selected','none'): err('Invalid quotes_required')
    by_id, dois, families = {}, {}, collections.defaultdict(list)
    core, full_core, verified_quotes = 0, 0, 0
    required = ('id','title','year','status','access','identity_verified','source_url','bibliography','relevance','design','findings','limitations','integrity','index_evidence','metrics','quotes')
    configured_levels = m.get('accepted_index_levels', ['direct_record','official_list'])
    if not isinstance(configured_levels,list) or not all(isinstance(x,str) for x in configured_levels):
        err('accepted_index_levels must be a list of strings'); configured_levels=[]
    levels = set(configured_levels)
    if m.get('max_quote_words') is not None and (type(m['max_quote_words']) is not int or m['max_quote_words']<1):
        err('max_quote_words must be a positive integer'); m=dict(m);m.pop('max_quote_words',None)
    for n,r in enumerate(records):
        if not isinstance(r, dict): err(f'Record {n} is not an object'); continue
        rid = str(r.get('id',f'row-{n}'))
        for f in required:
            if f not in r: err(f'{rid}: missing {f}')
        if rid in by_id: err(f'{rid}: duplicate ID')
        by_id[rid] = r
        if r.get('status') not in ('core','supplementary','excluded','awaiting_full_text'): err(rid+': invalid status')
        if r.get('access') not in ('full_text','abstract','metadata'): err(rid+': invalid access')
        if type(r.get('year')) is not int: err(rid+': missing/invalid publication year')
        for f in ('title','source_url','bibliography','relevance','design'):
            if not r.get(f): err(f'{rid}: empty {f}')
        malformed=False
        for f in ('findings','limitations','index_evidence','metrics','quotes'):
            if not isinstance(r.get(f,[]),list): err(f'{rid}: {f} must be a list');malformed=True
        if malformed: continue
        doi = normalized_doi(r.get('doi'))
        if doi:
            if doi in dois: err(f'{rid}: duplicate DOI with {dois[doi]}')
            dois[doi] = rid
        is_core = r.get('status') == 'core'
        core += int(is_core)
        full_core += int(is_core and r.get('access') == 'full_text')
        if is_core:
            if r.get('identity_verified') is not True: err(rid+': core identity not verified')
            if r.get('access') != 'full_text' and not m.get('allow_abstract_core',False): err(rid+': core lacks full text')
            if not r.get('findings'): err(rid+': core findings missing')
            if not r.get('limitations'): err(rid+': core limitations/appraisal missing')
            accepted = {x.get('name','').casefold() for x in r.get('index_evidence',[]) if isinstance(x,dict) and x.get('verified') is True and x.get('level') in levels and x.get('source') and valid_date(x.get('checked_on'))}
            requested = m.get('required_indexes',[])
            if isinstance(requested,list) and requested and not accepted.intersection(str(x).casefold() for x in requested): err(rid+': core does not meet required index evidence')
        integ = r.get('integrity',{})
        if not isinstance(integ,dict): integ={};err(rid+': integrity must be an object')
        if is_core and integ.get('status')=='retracted': err(rid+': retracted source in core')
        if integ.get('status') in ('not_checked',None): warnings.append(rid+': integrity not checked')
        elif not integ.get('source') or not valid_date(integ.get('checked_on')): err(rid+': integrity check lacks provenance')
        if integ.get('status')=='expression_of_concern': warnings.append(rid+': expression of concern requires adjudication')
        if is_core and r.get('study_family'): families[str(r['study_family'])].append(rid)
        for finding in r.get('findings',[]) if isinstance(r.get('findings',[]),list) else []:
            if not isinstance(finding,dict) or not finding.get('text') or not finding.get('locator') or finding.get('basis') not in ('author_report','reviewer_inference'): err(rid+': finding lacks text, locator or attribution')
        for limitation in r.get('limitations',[]) if isinstance(r.get('limitations',[]),list) else []:
            if not isinstance(limitation,dict) or not limitation.get('text') or limitation.get('basis') not in ('author_report','reviewer_inference'): err(rid+': limitation lacks attribution')
        for metric in r.get('metrics',[]) if isinstance(r.get('metrics',[]),list) else []:
            if not isinstance(metric,dict): err(rid+': invalid metric');continue
            v=metric.get('value')
            if v is not None:
                if type(v) not in (int,float) or not (0 <= v < float('inf')): err(rid+': invalid metric value')
                if not metric.get('provider') or not metric.get('source') or not valid_date(metric.get('observed_on')): err(rid+': observed metric lacks provenance')
            if metric.get('entity') not in ('work','venue','author'): err(rid+': invalid metric entity')
            if metric.get('name')=='journal_h_index' and metric.get('entity')!='venue': err(rid+': journal h assigned to wrong entity')
            if metric.get('name')=='citation_count' and metric.get('entity')!='work': err(rid+': article citations assigned to wrong entity')
        good_for_record=0
        for q in r.get('quotes',[]) if isinstance(r.get('quotes',[]),list) else []:
            before=len(errors)
            if not isinstance(q,dict): err(rid+': invalid quote');continue
            for f in ('text','source_text','source_url','version','citation'):
                if not q.get(f):err(f'{rid}: quote lacks {f}')
            if q.get('verified') is not True: err(rid+': delivered quote not verified')
            if r.get('access')!='full_text': err(rid+': quote without full-text access')
            if q.get('text') and normalized_text(q['text']) not in normalized_text(q.get('source_text','')): err(rid+': quote does not match inspected text')
            loc=q.get('locator',{})
            if not isinstance(loc,dict):loc={}
            if not (loc.get('printed_page') is not None or loc.get('pdf_page') is not None or loc.get('section')):err(rid+': quote lacks locator')
            if loc.get('pdf_page') is not None and (type(loc['pdf_page']) is not int or loc['pdf_page']<1):err(rid+': invalid PDF page')
            if m.get('max_quote_words') and len(str(q.get('text','')).split())>m['max_quote_words']:err(rid+': quote exceeds configured word budget')
            if len(errors)==before:good_for_record+=1;verified_quotes+=1
        if is_core and m.get('quotes_required')=='all_core' and good_for_record==0:err(rid+': required core quotation missing')
    if m.get('reported_core')!=core:err(f'Reported core count differs from actual {core}')
    if type(m.get('minimum_core')) is int and core<m['minimum_core']:err(f'Core shortfall: {core}/{m["minimum_core"]}')
    for family,ids in families.items():
        if len(ids)>1:warnings.append(f'Shared study family {family}: {", ".join(ids)}; not independent studies')
    claims=bundle.get('claims',[])
    if not isinstance(claims,list):err('claims must be a list');claims=[]
    for c in claims:
        if not isinstance(c,dict):err('Invalid claim');continue
        if not c.get('text') or not c.get('support_ids'):err(str(c.get('id'))+': claim lacks text/support')
        if not isinstance(c.get('support_ids',[]),list) or not isinstance(c.get('counter_ids',[]),list):err('Claim IDs must be lists');continue
        for rid in c.get('support_ids',[])+c.get('counter_ids',[]):
            if rid not in by_id:err(f'Claim {c.get("id")}: unknown record {rid}')
            elif by_id[rid].get('status')=='excluded':err(f'Claim {c.get("id")}: excluded source {rid} used as evidence')
    searches=bundle.get('searches',[])
    if not isinstance(searches,list):err('searches must be a list');searches=[]
    if not searches:warnings.append('No executed search/export log; do not claim systematic coverage')
    for s in searches:
        if not isinstance(s,dict) or not all(s.get(f) for f in ('id','provider','query','status')) or not valid_date(s.get('date')):err('Incomplete search log entry')
    return {'ok':not errors,'errors':errors,'warnings':warnings,'counts':{'reports':len(records),'core':core,'full_text_core':full_core,'verified_quotes':verified_quotes,'unique_dois':len(dois)}}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('bundle')
    parser.add_argument('--output')
    args=parser.parse_args()
    try:
        with open(args.bundle,encoding='utf-8') as f:result=validate(json.load(f))
    except (OSError,json.JSONDecodeError) as e:
        result={'ok':False,'errors':[str(e)],'warnings':[],'counts':{}}
    text=json.dumps(result,ensure_ascii=False,indent=2)
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:f.write(text+'\n')
    print(text)
    return 0 if result['ok'] else 1

if __name__=='__main__':sys.exit(main())
