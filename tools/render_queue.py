#!/usr/bin/env python3
"""Render completed self-contained movie sources; never infer visual acceptance."""
import argparse,datetime,fcntl,json,pathlib,re,shutil,subprocess,sys,time
from catalog import ROOT,dump
from generate import record
HF=str(ROOT/'node_modules/.bin/hyperframes')
def parse_check(text):
 decoder=json.JSONDecoder()
 for m in re.finditer(r'(?m)^\{',text):
  try:value,_=decoder.raw_decode(text[m.start():])
  except ValueError:continue
  if isinstance(value,dict) and 'ok' in value and 'browserSkipped' in value:return value
 raise ValueError('No HyperFrames check report in command output')
def run(command,log,timeout=1200):
 with log.open('w') as out:
  return subprocess.run(command,cwd=ROOT,stdout=out,stderr=subprocess.STDOUT,timeout=timeout).returncode

def render(v,track,r):
 slug=v['slug'];out=ROOT/'work/render-queue'/slug/track;out.mkdir(parents=True,exist_ok=True)
 source=(ROOT/'results'/slug/track/'index.html').read_text()
 if v['category']=='interactive':return 'Interactive controls and deterministic replay need a separate test before recording a comparison movie.'
 if re.search(r'''(?:src|href)\s*=\s*["']https?://|url\(\s*["']?https?://|\bfetch\s*\(|\bimport\s*\(''',source,re.I):return 'External runtime dependencies must be reviewed and frozen locally before rendering.'
 if shutil.disk_usage(ROOT).free<10*1024**3:raise RuntimeError('Less than 10 GiB disk space remains; render queue stopped.')
 project=ROOT/'work/render-projects'/slug/track;check=out/'check.json';movie=out/'video.mp4'
 if run([sys.executable,str(ROOT/'tools/prepare_render.py'),slug,'--track',track],out/'prepare.log'):return 'Staging failed; inspect local render-queue diagnostics.'
 if run([HF,'check',str(project),'--snapshots','--json'],check):return 'Technical browser check failed; source retained for a recorded repair.'
 report=parse_check(check.read_text());dump(check,report)
 if not report.get('ok'):return 'Technical browser check did not pass.'
 if run([HF,'render',str(project),'--quality','looks','--workers','2','--output',str(movie)],out/'render.log'):return 'Video render failed; inspect local render-queue diagnostics.'
 if run([sys.executable,str(ROOT/'tools/attach_render.py'),slug,'--track',track,'--video',str(movie),'--check',str(check)],out/'attach.log'):return 'Render attachment verification failed.'
 # Source remains generated/rendered, never visually reviewed by this worker.
 return None
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--watch',action='store_true');p.add_argument('--track',choices=['baseline','adapted'],default='baseline');a=p.parse_args()
 (ROOT/'work').mkdir(exist_ok=True)
 with (ROOT/'work/render-queue.lock').open('w') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  while True:
   catalog=json.loads((ROOT/'data/catalog.json').read_text());processed=0
   for v in catalog:
    path=ROOT/'results'/v['slug']/'result.json'
    if not path.exists():continue
    r=json.loads(path.read_text()).get(a.track,{})
    if r.get('status')!='generated' or r.get('render_queue_reason'):continue
    try:reason=render(v,a.track,r)
    except Exception as e:reason='Render supervisor error: '+str(e)
    processed+=1
    if reason:
     r.update(render_queue_reason=reason);record(v['slug'],a.track,r)
    print(json.dumps({'slug':v['slug'],'track':a.track,'rendered':reason is None,'reason':reason,'at':datetime.datetime.now(datetime.timezone.utc).isoformat()}),flush=True)
    subprocess.run([sys.executable,str(ROOT/'tools/catalog.py')],cwd=ROOT,stdout=subprocess.DEVNULL,check=True)
   if not a.watch:break
   progress=ROOT/'work/batch-baseline-progress.json'
   if progress.exists() and json.loads(progress.read_text()).get('finished_at') and not processed:break
   time.sleep(20)
