#!/usr/bin/env python3
"""Execute a resumable corpus queue and rebuild the gallery on every finished entry."""
import argparse,concurrent.futures,datetime,json,pathlib,subprocess,sys,threading
from catalog import ROOT,dump
STOP=threading.Event()
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def state(v,track):
 p=ROOT/'results'/v['slug']/'result.json'
 return json.loads(p.read_text()).get(track,{}).get('status','not_generated') if p.exists() else 'not_generated'
def run(v,a):
 if STOP.is_set():return {'slug':v['slug'],'status':'not_started'}
 slug=v['slug'];out=ROOT/'work/batch-logs'/a.track;out.mkdir(parents=True,exist_ok=True)
 with (out/f'{slug}.log').open('w') as f:
  command=[sys.executable,str(ROOT/'tools/generate.py'),slug,'--track',a.track,'--timeout',str(a.timeout),'--execute']
  if a.research:command+=['--research']
  r=subprocess.run(command,cwd=ROOT,stdout=f,stderr=subprocess.STDOUT)
 status=state(v,a.track)
 error=''
 if r.returncode:
  events=ROOT/'results'/slug/a.track/'events.jsonl'
  if events.exists():
   messages=[]
   for l in events.read_text().splitlines():
    try:
     e=json.loads(l)
     if e.get('type') in ('error','turn.failed'):messages.append(str(e.get('message') or e.get('error')))
    except ValueError:pass
   error=' '.join(messages)[-2000:]
  if any(w in error.lower() for w in ['usage limit','rate limit','rate_limit','quota','not supported','authentication','unauthorized','insufficient','credit','login']):STOP.set()
 subprocess.run([sys.executable,str(ROOT/'tools/catalog.py')],cwd=ROOT,stdout=subprocess.DEVNULL,check=True)
 row={'slug':slug,'track':a.track,'status':status,'finished_at':now(),'returncode':r.returncode,'provider_error':error}
 print(json.dumps(row),flush=True);return row
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--track',choices=['baseline','adapted'],default='baseline');p.add_argument('--workers',type=int,default=2);p.add_argument('--timeout',type=int,default=900);p.add_argument('--execute',action='store_true');p.add_argument('--research',action='store_true');p.add_argument('--slugs',nargs='*');a=p.parse_args()
 catalog=json.loads((ROOT/'data/catalog.json').read_text());rows=[v for v in catalog if state(v,a.track)=='not_generated' and (not a.slugs or v['slug'] in a.slugs)]
 # Start with references already available and self-contained prompts; every remaining entry stays in the queue.
 rows.sort(key=lambda v:(not v['showcased'],not bool(v['reference'].get('video_url')),v['prompt_partial'],len(v['dependency_cues'])))
 progress={'started_at':now(),'track':a.track,'model':'gpt-6.1-sol','reasoning_effort':'high','requested_entries':len(rows),'workers':a.workers,'completed':[],'stopped_on_provider_error':False}
 print(json.dumps({'queued':len(rows),'track':a.track,'first':[v['slug'] for v in rows[:15]]}),flush=True)
 if not a.execute:sys.exit()
 path=ROOT/'work'/f'batch-{a.track}-progress.json';dump(path,progress)
 with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:
  pending={};iterator=iter(rows)
  for _ in range(a.workers):
   v=next(iterator,None)
   if v:pending[pool.submit(run,v,a)]=v
  while pending:
   done,_=concurrent.futures.wait(pending,return_when=concurrent.futures.FIRST_COMPLETED)
   for future in done:
    v=pending.pop(future)
    try:result=future.result()
    except Exception as e:result={'slug':v['slug'],'status':'supervisor_error','error':str(e)};STOP.set()
    progress['completed'].append(result);progress['stopped_on_provider_error']=STOP.is_set();dump(path,progress)
    if not STOP.is_set():
     v=next(iterator,None)
     if v:pending[pool.submit(run,v,a)]=v
 progress['finished_at']=now();dump(path,progress)
