#!/usr/bin/env python3
"""Publish the authorized corpus worker outputs as progress changes."""
import argparse,json,os,pathlib,subprocess,time
from catalog import ROOT
from github_sync import repo
PATHS=['results','docs','data/catalog.json','data/audit.json','provenance/INVENTORY.md']
def command(args,**kwargs):return subprocess.run(args,cwd=ROOT,check=True,**kwargs)
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--watch',action='store_true');a=p.parse_args()
 if repo()!='valekar/awesome-gpt-videos':raise RuntimeError('Unexpected publication destination')
 last=None
 while True:
  raw=(ROOT/'docs/progress.json').read_text();counts=json.loads(raw)
  key=json.dumps([counts['run_counts'],counts['sampled_reviews'],counts['visual_reviewed']],sort_keys=True)
  if key!=last:
   branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip()
   if branch!='main':raise RuntimeError('Publication requires main')
   if subprocess.run(['git','diff','--cached','--quiet'],cwd=ROOT).returncode:raise RuntimeError('Existing staged work preserved; publisher stopped')
   command(['npm','test']);command(['git','add','--',*PATHS])
   if subprocess.run(['git','diff','--cached','--quiet'],cwd=ROOT).returncode:
    # Exact creator inputs and model responses may contain trailing whitespace.
    # Preserve their hashes; provenance tests, rather than formatting, gate publication.
    command(['git','commit','-m','Update corpus generation and render progress'])
    command(['python3','tools/github_sync.py','--push'])
   last=key
  if not a.watch:break
  progress=ROOT/'work/batch-baseline-progress.json'
  finished=progress.exists() and json.loads(progress.read_text()).get('finished_at')
  if finished:
   # Allow the render worker to drain; it marks render reasons for gated sources.
   entries=json.loads((ROOT/'data/catalog.json').read_text())
   if not any(r.get('status')=='generated' and not r.get('render_queue_reason') for v in entries for t,r in v['runs'].items() if t=='baseline'):break
  time.sleep(120)
