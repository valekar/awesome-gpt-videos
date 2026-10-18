#!/usr/bin/env python3
"""Draft a GPT-6.1/high reference reconstruction from declared decoded frame evidence."""
import argparse,json,pathlib,subprocess,sys,hashlib
from catalog import ROOT,dump,digest
from reference_frames import prepare
SCHEMA={'type':'object','additionalProperties':False,'properties':{'brief_markdown':{'type':'string'},'observed_scenes':{'type':'array','items':{'type':'object','additionalProperties':False,'properties':{'start_seconds':{'type':'number'},'end_seconds':{'type':'number'},'description':{'type':'string'}},'required':['start_seconds','end_seconds','description']}},'exact_visible_text':{'type':'array','items':{'type':'string'}},'uncertainties':{'type':'array','items':{'type':'string'}},'missing_inputs':{'type':'array','items':{'type':'string'}},'audio_review':{'type':'string'}},'required':['brief_markdown','observed_scenes','exact_visible_text','uncertainties','missing_inputs','audio_review']}
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('slug');a=p.parse_args();v=next(v for v in json.loads((ROOT/'data/videos.json').read_text()) if v['slug']==a.slug)
 base=ROOT/'work/references'/a.slug;out=ROOT/'work/reference-audits'/a.slug;out.mkdir(parents=True,exist_ok=True)
 evidence=json.loads((base/'evidence.json').read_text()) if (base/'evidence.json').exists() else prepare(a.slug)
 prompt='''Analyze the attached decoded-frame evidence from the complete duration of an existing creator video. No tools, shell, private files, web access or agents. Write a detailed timed reconstruction brief for a NEW code-rendered recreation. This is inferred reference guidance, never the creator's identical original prompt. Read timestamp labels and distinguish the boundaries of contact-sheet tiles. Inspect full-resolution frames for left/right layout, scale, typography and fine geometry. Preserve every distinct observed shot, action, transition, exact visible text, quantities, language, aspect and duration. Do not infer motion from a single still or invent missing scenes. State uncertainty between sampled frames. Describe geometry, material, palette, visual density, camera/crop, layering, and entry/exit motion. Reference images may not be reused as output artwork. Unknown private inputs must remain unknown. Values shown in the reference are visual evidence, not independently verified factual claims. If audio_streams>0, audio was NOT supplied to this analysis: explicitly say sound/narration has not been reviewed; do not invent what is audible or mark the film silent. Document required follow-up. If partial creator material can be reconstructed visually, label it inferred rather than unavailable original chat. Return only the schema JSON.\n\nCREATOR MATERIAL:\n'''+v['prompt']+'\n\nFROZEN REFERENCE METADATA:\n'+json.dumps(evidence)
 (out/'input.txt').write_text(prompt);dump(out/'schema.json',SCHEMA)
 images=[ROOT/p for p in evidence['sheets']+evidence['full_frames']]
 command=['npx','--yes','@openai/codex@0.163.0','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check','--model','gpt-6.1-sol','-c','model_reasoning_effort="high"','--sandbox','read-only','--json','--output-schema',str(out/'schema.json'),'-o',str(out/'response.json')]
 for image in images:command+=['--image',str(image)]
 command+=['-']
 with (out/'events.jsonl').open('w') as events,(out/'stderr.log').open('w') as err:
  result=subprocess.run(command,input=prompt,text=True,cwd=ROOT,stdout=events,stderr=err,timeout=900)
 if result.returncode:raise RuntimeError('Reference analysis failed; inspect local diagnostic logs')
 reply=json.loads((out/'response.json').read_text());usage={}
 for line in (out/'events.jsonl').read_text().splitlines():
  event=json.loads(line)
  if event.get('type')=='turn.completed':usage=event.get('usage',{})
  if event.get('item',{}).get('type') in ('command_execution','mcp_tool_call','web_search'):raise RuntimeError('Unexpected tool use in reference analysis')
 dest=ROOT/'comparison/reference-audits'/a.slug;dest.mkdir(parents=True,exist_ok=True)
 dump(dest/'analysis.json',reply);dump(dest/'provenance.json',{'model':'gpt-6.1-sol','reasoning_effort':'high','review_type':'model-generated sampled visual analysis','input_sha256':digest(prompt),'reference_evidence':evidence,'image_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in images},'usage':usage,'audio_supplied':False})
 brief=ROOT/'comparison/matched-briefs'/f'{a.slug}.md'
 if brief.exists():raise RuntimeError('Existing matched brief preserved; new draft is in reference-audits for reconciliation')
 brief.write_text('# Model-drafted reference reconstruction — '+a.slug+'\n\nStatus: sampled visual reconstruction; full timing/audio acceptance pending. Generated with GPT-6.1 Sol/high from declared reference frames.\n\n'+reply['brief_markdown']+'\n\n## Observed scene samples\n'+ '\n'.join(f"- {r['start_seconds']}–{r['end_seconds']}s: {r['description']}" for r in reply['observed_scenes'])+'\n\n## Visible text evidence\n'+ '\n'.join('- '+r for r in reply['exact_visible_text'])+'\n\n## Declared uncertainties\n'+ '\n'.join('- '+s for s in reply['uncertainties'])+'\n\nAudio: '+reply['audio_review']+'\n')
 print(brief.relative_to(ROOT))
