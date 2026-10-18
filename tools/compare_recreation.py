#!/usr/bin/env python3
"""Compare original/new decoded frames at shared times with attributed GPT review."""
import argparse,hashlib,json,math,pathlib,subprocess,sys
from PIL import Image,ImageDraw
from catalog import ROOT,dump,digest
SCHEMA={'type':'object','additionalProperties':False,'properties':{
 'summary':{'type':'string'},'matches':{'type':'array','items':{'type':'string'}},
 'differences':{'type':'array','items':{'type':'object','additionalProperties':False,'properties':{'time_seconds':{'type':'number'},'description':{'type':'string'},'severity':{'type':'string','enum':['minor','major']},'actionable':{'type':'boolean'}},'required':['time_seconds','description','severity','actionable']}},
 'revision_feedback':{'type':'string'},'should_revise':{'type':'boolean'},'prompt_improvement_markdown':{'type':'string'},'limitations':{'type':'array','items':{'type':'string'}}},'required':['summary','matches','differences','revision_feedback','should_revise','prompt_improvement_markdown','limitations']}
def evidence(slug,iteration):
 base=ROOT/'work/references'/slug;ref=json.loads((base/'evidence.json').read_text());out=ROOT/'work/comparison-evidence'/slug/f'{iteration:03d}';out.mkdir(parents=True,exist_ok=True)
 movie=ROOT/'docs/media'/slug/'adapted/video.mp4'
 duration=ref['duration_seconds'];times=set(ref['sample_times'])
 for t in ref['scene_change_times']:
  for offset in [-.1,0,.1]:times.add(round(max(0,min(duration-.05,t+offset)),4))
 times=sorted(times|{round(max(0,duration-.15),4)})
 pairs=[]
 for i,t in enumerate(times):
  pair=[]
  for name,src in [('original',base/'original.mp4'),('gpt',movie)]:
   path=out/f'{i:04d}-{name}.jpg'
   subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss',str(t),'-i',str(src),'-frames:v','1','-q:v','2',str(path)],check=True)
   pair.append(path)
  pairs.append(pair)
 sheets=[]
 for page in range(math.ceil(len(times)/8)):
  group=pairs[page*8:(page+1)*8];tile_w=480;tile_h=round(ref['height']/ref['width']*tile_w);canvas=Image.new('RGB',(1920,4*(tile_h+27)),(25,25,25));draw=ImageDraw.Draw(canvas)
  for j,pair in enumerate(group):
   t=times[page*8+j]
   for k,path in enumerate(pair):
    x=(j%2*2+k)*tile_w;y=j//2*(tile_h+27);im=Image.open(path).convert('RGB');im.thumbnail((tile_w,tile_h));canvas.paste(im,(x,y+27));draw.text((x+7,y+5),f'{"ORIGINAL" if k==0 else "GPT"} | requested t={t:.4f}s',fill='white')
  path=out/f'sheet-{page+1:02d}.jpg';canvas.save(path,quality=90);sheets.append(path)
 details=[]
 for i in sorted({0,len(times)//2,len(times)-1}):
  ims=[Image.open(p).convert('RGB') for p in pairs[i]];w,h=ims[0].size;canvas=Image.new('RGB',(w*2,h+35),(25,25,25));draw=ImageDraw.Draw(canvas)
  for k,im in enumerate(ims):
   if im.size!=(w,h):im=im.resize((w,h))
   canvas.paste(im,(k*w,35));draw.text((k*w+10,10),f'{"ORIGINAL" if k==0 else "GPT"} | requested t={times[i]:.4f}s',fill='white')
  path=out/f'detail-{i:04d}.jpg';canvas.save(path,quality=94);details.append(path)
 return {'times':times,'reference_metadata':ref,'sheets':[str(p.relative_to(ROOT)) for p in sheets],'details':[str(p.relative_to(ROOT)) for p in details],'sampling':'Requested matching seek times; video frames are quantized to each stream frame rate. No audio supplied.'}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('slug');a=p.parse_args();meta=json.loads((ROOT/'results'/a.slug/'adapted/metadata.json').read_text());iteration=meta['iteration'];out=ROOT/'work/comparison-model'/a.slug/f'{iteration:03d}';out.mkdir(parents=True,exist_ok=True)
 ev=evidence(a.slug,iteration);dump(out/'evidence.json',ev)
 prompt='''Compare the supplied ORIGINAL and GPT decoded film frames. No tools, web, files, shell or agents. Each two adjacent tiles are a pair at the same requested timestamp. Black label strips and blank sheet cells are evidence scaffolding, not artwork. Full-resolution detail pairs show finer layout/text; inspect them. Assess scene coverage, exact text/brands/quantities, typography, layout, subject geometry, layering, timing, motion states, camera, and important missing visual mechanisms. Do not invent motion between still samples. Record concrete differences with timestamps and severity; separate actionable major differences from uncertain font identity or tiny pixel differences. Suggest a focused source/prompt revision preserving correct parts, only when evidence supports it. Do not ask to paste or reuse reference frames, original scene code, logos/photos without rights, or audio from the source. Values in the original are visual claims, not independently verified facts. These are model-generated sampled findings, NOT a human review, frame-by-frame acceptance, quality score or model ranking. Audio is not supplied; say so even if an audio stream is reported. If no reference audio stream exists, report both technical stream evidence and silence without claiming listening. All limitations belong in the output. Return the schema.\n\nREFERENCE AND SAMPLING:\n'''+json.dumps(ev)+'\n\nTIMED RECONSTRUCTION:\n'+(ROOT/'comparison/matched-briefs'/f'{a.slug}.md').read_text()+'\n\nATTEMPT METADATA:\n'+json.dumps(meta)
 (out/'input.txt').write_text(prompt);dump(out/'schema.json',SCHEMA)
 images=[ROOT/p for p in ev['sheets']+ev['details']]
 command=['npx','--yes','@openai/codex@0.163.0','exec','--ignore-user-config','--ephemeral','--model','gpt-6.1-sol','-c','model_reasoning_effort="high"','--sandbox','read-only','--json','--output-schema',str(out/'schema.json'),'-o',str(out/'response.json')]
 for image in images:command+=['--image',str(image)]
 command+=['-']
 with (out/'events.jsonl').open('w') as log,(out/'stderr.log').open('w') as err:
  result=subprocess.run(command,input=prompt,text=True,cwd=ROOT,stdout=log,stderr=err,timeout=900)
 if result.returncode:raise RuntimeError('Comparison model failed; inspect private diagnostics')
 usage={}
 for line in (out/'events.jsonl').read_text().splitlines():
  event=json.loads(line)
  if event.get('type')=='turn.completed':usage=event.get('usage',{})
  if event.get('item',{}).get('type') in ['command_execution','mcp_tool_call','web_search']:raise RuntimeError('Unexpected tool call in sampled comparison')
 reply=json.loads((out/'response.json').read_text());review=ROOT/'comparison/reviews'/f'{a.slug}.json';existing=json.loads(review.read_text()) if review.exists() else {'slug':a.slug}
 history=existing.get('adapted_review_history',[])
 history.append({'iteration':iteration,**reply,'model':'gpt-6.1-sol','reasoning_effort':'high','input_sha256':digest(prompt),'image_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in images},'evidence':ev,'usage':usage})
 existing.update(status='sampled',reviewer='GPT-6.1 Sol/high automated matched-time frame comparison',method=ev['sampling'],adapted={'attempts':iteration,'observations':reply['matches'],'remaining_differences':[d['description'] for d in reply['differences']]},adapted_review_history=history,summary=reply['summary'],limitations=reply['limitations'],reference=ev['reference_metadata'])
 dump(review,existing);dump(ROOT/'docs/reviews'/f'{a.slug}.json',existing)
 improvements=ROOT/'comparison/prompt-improvements'/f'{a.slug}.md';improvements.parent.mkdir(parents=True,exist_ok=True)
 with improvements.open('a') as f:f.write(f'\n\n## Matched-time review of attempt {iteration}\n\n'+reply['prompt_improvement_markdown']+'\n')
 (out/'feedback.txt').write_text(reply['revision_feedback'])
 subprocess.run([sys.executable,str(ROOT/'tools/catalog.py')],cwd=ROOT,stdout=subprocess.DEVNULL,check=True)
 print(json.dumps({'slug':a.slug,'iteration':iteration,'should_revise':reply['should_revise'],'feedback':str((out/'feedback.txt').relative_to(ROOT))}),flush=True)
