#!/usr/bin/env python3
"""Prioritize reference-led recreations, technical renders and sampled comparisons."""
import argparse,datetime,fcntl,json,pathlib,re,subprocess,sys
from catalog import ROOT,dump
from render_queue import render
NATIVE=re.compile(r'\b(Blender|Manim|Raylib|Remotion|C/C\+\+)\b',re.I)
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def classify(v):
 if v['runs']['adapted'].get('status') in ('rendered','reviewed'):
  return 'existing_render' if v.get('review',{}).get('adapted') else 'render_needs_comparison'
 if v['runs']['adapted'].get('status')=='blocked':return 'missing_inputs_or_workflow'
 path=ROOT/'work/references'/v['slug']/'reference.json'
 if not path.exists():return 'reference_unavailable'
 ref=json.loads(path.read_text())
 if ref.get('status')!='downloaded':return 'reference_download_failed'
 if NATIVE.search(v['prompt']):return 'native_renderer_route'
 if v['category']=='interactive':return 'interactive_replay_needed'
 if any(s['codec_type']=='audio' for s in ref['probe']['streams']):return 'audio_review_needed'
 return 'ready_for_visual_recreation'
def state(slug):
 p=ROOT/'results'/slug/'result.json'
 return json.loads(p.read_text()).get('adapted',{}) if p.exists() else {'status':'not_generated'}
def queue():
 rows=json.loads((ROOT/'data/catalog.json').read_text())
 result=[{'slug':v['slug'],'stage':classify(v)} for v in rows]
 dump(ROOT/'docs/adapted-queue.json',{'priority':'adapted','model':'gpt-6.1-sol','reasoning_effort':'high','updated_at':now(),'entries':result})
 return rows,result
def command(args,folder,name):
 folder.mkdir(parents=True,exist_ok=True)
 with (folder/(name+'.log')).open('w') as f:r=subprocess.run([sys.executable,*map(str,args)],cwd=ROOT,stdout=f,stderr=subprocess.STDOUT)
 if r.returncode:raise RuntimeError(name+' failed; inspect '+str((folder/(name+'.log')).relative_to(ROOT)))
def _process(v,a):
 slug=v['slug'];folder=ROOT/'work/adapted-queue'/slug
 meta=ROOT/'work/references'/slug/'evidence.json'
 if not meta.exists():command(['tools/reference_frames.py',slug],folder,'reference')
 brief=ROOT/'comparison/matched-briefs'/f'{slug}.md'
 if not brief.exists():command(['tools/analyze_reference.py',slug],folder,'analysis')
 ev=json.loads(meta.read_text());images=[]
 for p in ev['sheets']+ev['full_frames']:images+=['--image',p]
 r=state(slug)
 if r.get('status')=='running':raise RuntimeError('Entry already has an active generation; leave its artifacts untouched')
 if r.get('status') not in ('generated','rendered','reviewed'):
  command(['tools/generate.py',slug,'--track','adapted',*images,'--execute'],folder,'generation')
 r=state(slug)
 if r.get('status')=='blocked':return {'slug':slug,'stage':'blocked','reason':r.get('reason')}
 for revision in range(a.max_revisions+1):
  r=state(slug)
  if r['status']=='generated':
   reason=render(v,'adapted',r)
   if reason:
    # A technical failure is repaired by the requested model, never silently hand-edited.
    if revision==a.max_revisions:return {'slug':slug,'stage':'technical_repair_needed','reason':reason}
    check=ROOT/'work/render-queue'/slug/'adapted/check.json'
    feedback=folder/'technical-feedback.txt';feedback.write_text('Repair the technical issues while preserving reference coverage. '+reason+'\n'+(check.read_text() if check.exists() else ''))
    command(['tools/generate.py',slug,'--track','adapted','--revise',feedback,*images,'--execute'],folder,f'technical-revision-{revision+1}');continue
  command(['tools/compare_recreation.py',slug],folder,f'comparison-{state(slug).get("iteration",1)}')
  review=json.loads((ROOT/'comparison/reviews'/f'{slug}.json').read_text())['adapted_review_history'][-1]
  if not review['should_revise'] or revision==a.max_revisions:break
  feedback=ROOT/'work/comparison-model'/slug/f"{review['iteration']:03d}"/'feedback.txt'
  command(['tools/generate.py',slug,'--track','adapted','--revise',feedback,*images,'--execute'],folder,f'visual-revision-{revision+1}')
 return {'slug':slug,'stage':'sampled_comparison_saved','iterations':state(slug).get('iteration',1),'full_acceptance':False}
def process(v,a):
 lock=ROOT/'results'/v['slug']/'adapted/workflow.lock';lock.parent.mkdir(parents=True,exist_ok=True)
 with lock.open('w') as handle:
  fcntl.flock(handle,fcntl.LOCK_EX|fcntl.LOCK_NB)
  return _process(v,a)
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--execute',action='store_true');p.add_argument('--max-revisions',type=int,default=1);p.add_argument('--slugs',nargs='*');a=p.parse_args()
 rows,stages=queue();mapping={r['slug']:r['stage'] for r in stages}
 rows=[v for v in rows if mapping[v['slug']] in ('ready_for_visual_recreation','render_needs_comparison') and (not a.slugs or v['slug'] in a.slugs)]
 rows.sort(key=lambda v:(v['runs']['adapted'].get('status') not in ('generated','rendered'),not (ROOT/'comparison/matched-briefs'/f"{v['slug']}.md").exists(),not v['showcased'],float(json.loads((ROOT/'work/references'/v['slug']/'reference.json').read_text())['probe']['format']['duration'])))
 print(json.dumps({'queued':len(rows),'stages':{s:sum(x['stage']==s for x in stages) for s in sorted(set(x['stage'] for x in stages))},'first':[v['slug'] for v in rows[:10]]}),flush=True)
 if not a.execute:sys.exit()
 with (ROOT/'work/adapted-queue.lock').open('w') as lock:
  fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
  progress={'priority':'adapted','model':'gpt-6.1-sol','reasoning_effort':'high','started_at':now(),'completed':[],'current':None};path=ROOT/'work/adapted-priority-progress.json';dump(path,progress)
  for v in rows:
   progress['current']=v['slug'];dump(path,progress)
   try:r=process(v,a)
   except Exception as e:
    progress['error']=str(e);progress['stopped_at']=now();dump(path,progress);raise
   progress['completed'].append(r);print(json.dumps(r),flush=True);dump(path,progress)
   queue();subprocess.run([sys.executable,str(ROOT/'tools/catalog.py')],cwd=ROOT,stdout=subprocess.DEVNULL,check=True)
  progress.update(current=None,finished_at=now());dump(path,progress)
