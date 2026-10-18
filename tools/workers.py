#!/usr/bin/env python3
"""Start or inspect detached, PID-tracked corpus workers (ordinary OS processes)."""
import argparse,datetime,fcntl,json,os,pathlib,re,shutil,subprocess,sys
from catalog import ROOT,dump
from generate import record
REGISTRY=ROOT/'work/workers.json'
def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def alive(pid,script):
 result=subprocess.run(['ps','-p',str(pid),'-o','stat=,args='],capture_output=True,text=True)
 return result.returncode==0 and not result.stdout.lstrip().startswith('Z') and script in result.stdout

def status():
 rows=json.loads(REGISTRY.read_text()) if REGISTRY.exists() else {}
 for role,r in rows.items():
  r['alive']=alive(r['pid'],r['script'])
  log=ROOT/r['log'];r['log_updated_at']=datetime.datetime.fromtimestamp(log.stat().st_mtime,datetime.timezone.utc).isoformat() if log.exists() else None
 return rows

def archive_interrupted():
 process_text=subprocess.check_output(['ps','-eo','args='],text=True)
 stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
 progress=ROOT/'work/batch-baseline-progress.json'
 if progress.exists():
  history=ROOT/'work/batch-history';history.mkdir(exist_ok=True);shutil.copyfile(progress,history/f'{stamp}.json')
 for p in (ROOT/'results').glob('*/result.json'):
  for track,r in json.loads(p.read_text()).items():
   if r.get('status')!='running' or track!='adapted':continue
   if f'tools/generate.py {p.parent.name} --track {track}' in process_text:continue
   folder=p.parent/track;archive=folder/'iterations'/('interrupted-'+stamp);archive.mkdir(parents=True,exist_ok=False)
   for name in ['input.txt','schema.json','events.jsonl','stderr.log','metadata.json','response.json']:
    if (folder/name).exists():shutil.copyfile(folder/name,archive/name)
   dump(archive/'interruption.json',{'previous_state':r,'detected_at':utc(),'reason':'No corresponding corpus worker process remains; previous execution has no completion event.'})
   record(p.parent.name,track,{'status':'not_generated','reason':'Interrupted worker attempt archived before resuming.','previous_attempt':str(archive.relative_to(ROOT)),'model':'gpt-6.1-sol','reasoning_effort':'high'})

def start(roles=None):
 (ROOT/'work').mkdir(exist_ok=True)
 with (ROOT/'work/workers-start.lock').open('w') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  process_text=subprocess.check_output(['ps','-eo','args='],text=True)
  if any(re.search(r'python[^ ]* (?:[^ ]*/)?tools/'+script+r'(?: |$)',process_text) for script in [{'generation':'adapted_queue.py','render':'render_queue.py','publication':'publish_progress.py'}[r] for r in (roles or ['generation','publication'])]):
   raise RuntimeError('A corpus worker already exists; inspect it before starting another set.')
  if not roles or 'generation' in roles:archive_interrupted()
  subprocess.run([sys.executable,str(ROOT/'tools/catalog.py')],cwd=ROOT,stdout=subprocess.DEVNULL,check=True)
  jobs={
   'generation':['tools/adapted_queue.py','--execute','--max-revisions','1'],
   'render':['tools/render_queue.py','--watch'],
   'publication':['tools/publish_progress.py','--watch']}
  registry=json.loads(REGISTRY.read_text()) if REGISTRY.exists() else {}
  if not roles and 'render' in registry and not alive(registry['render']['pid'],registry['render']['script']):registry.pop('render')
  for role,args in jobs.items():
   if role not in (roles or ['generation','publication']):continue
   log=ROOT/'work'/f'worker-{role}.log'
   with log.open('a') as out:
    out.write('\nWorker launched '+utc()+'\n');out.flush()
    child=subprocess.Popen([sys.executable,'-u',*args],cwd=ROOT,stdin=subprocess.DEVNULL,stdout=out,stderr=subprocess.STDOUT,start_new_session=True,close_fds=True,env=dict(os.environ,PYTHONUNBUFFERED='1'))
   registry[role]={'pid':child.pid,'script':args[0],'command':[sys.executable,*args],'started_at':utc(),'log':str(log.relative_to(ROOT))}
  dump(REGISTRY,registry)
 return status()
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('action',choices=['status','start']);p.add_argument('--role',choices=['generation','render','publication'],action='append');a=p.parse_args()
 print(json.dumps(start(a.role) if a.action=='start' else status(),indent=2))
