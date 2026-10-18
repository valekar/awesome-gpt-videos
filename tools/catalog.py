#!/usr/bin/env python3
"""Build auditable GPT prompt adaptations and the static comparison catalog."""
import argparse, collections, hashlib, json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[1]
MODEL = 'gpt-6.1-sol'
UPSTREAM = 'https://github.com/yihui-dev/awesome-opus5-5-videos'
CATEGORY = {
 'motion': 'Preserve visual hierarchy, exact UI states, typography, beat grid, morph continuity and loop seam. Inspect all transition states as well as settled frames.',
 'explainer': 'Preserve the complete explanatory sequence, language, narration, quantities, labels and causal demonstrations. Do not replace a mechanism with decorative text.',
 '3d': 'Preserve geometry, materials, lighting, camera path, subject scale, scene density and physical interactions. Inspect near and far surfaces and important occlusions.',
 'interactive': 'Preserve controls, game mechanics, physics, progression and HUD. Deliver a playable version plus a deterministic replay for video comparison; a scripted movie alone does not satisfy this prompt.'
}
TECH = {
 'canvas':'Recompute Canvas state from time; reset transforms and compositing on every frame.',
 'svg':'Keep vector geometry and typography sharp at the reference viewport.',
 'gsap':'Use a paused seekable GSAP timeline; use explicit initial values and deterministic seeks.',
 'threejs':'Use a fixed timestep or analytic scene state, seeded randomness, and a reproducible camera.',
 'glsl':'Drive shader time from the supplied render time and keep shader inputs reproducible.',
 'webgl':'Record renderer, GPU and shader dependencies; verify output in the rendering browser.',
 'audio':'Preserve required audio and measure cue timing; do not silently output a silent version.',
 'shader':'Drive shader uniforms from deterministic timeline time and verify rendering on the target browser/GPU.',
 'web-audio':'Keep audio cues, beat positions and gain in a separate reproducible timeline.',
 'ai-image':'Record the image model, source assets and generation prompt separately; do not attribute externally generated images to the coding model.'
}
CUES = {
 'attachment_or_reference': r'\b(attached|attachment|uploaded|reference (?:video|image|file)|included an MP4|screenshots?|provided (?:image|video|file))\b|添付|附件|参考视频',
 'private_project_context': r'\b(my app|my studio|my product|this project|this repo|the codebase|your codebase|about me|about my|our (?:app|product)|/asic|skill mesh)\b|本项目',
 'audio_dependency': r'\b(exact same audio|audio track|song|music|voiceover|narration|tts|soundtrack|ElevenLabs)\b|配音|音楽',
 'native_renderer': r'\b(Blender|Manim|Raylib|Remotion|C/C\+\+)\b',
 'input_request': r'\b(ask me for|ask me|your product|product link|company name)\b',
}
def digest(s): return hashlib.sha256(s.encode()).hexdigest()
def dump(path, obj):
 path.parent.mkdir(parents=True, exist_ok=True);path.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
def adapt(v, flags):
 tech=' '.join(TECH[t] for t in v['tech_tags'] if t in TECH)
 coverage=('The upstream entry is marked partial: this may be a post or incomplete instructions. Treat it as partial evidence; never call an inferred reconstruction the original prompt.' if v['prompt_partial'] else 'Upstream marks this as a full prompt. This does not establish that all referenced assets or prior chat context are available.')
 return f'''# GPT-6.1 high adaptation — {v['slug']}

Target model: `{MODEL}`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @{v['author']}. Source: {v['post_url']}
Reference page: {v['skillry_url']}
Original prompt SHA-256: `{digest(v['prompt'])}`.

## Source completeness

{coverage}
Dependency cues found by automated text inspection: {', '.join(flags) or 'none detected; manual reference review still required'}.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

{CATEGORY[v['category']]}

Upstream remake implementation tags (descriptive, not proof of the original stack): {', '.join(v['tech_tags']) or 'unspecified'}.{(' '+tech) if tech else ''}

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
{v['prompt']}
</creator_material>
'''
def build():
 videos=json.loads((ROOT/'data/videos.json').read_text());readme=(ROOT/'provenance/UPSTREAM_README.md').read_text()
 showcased=set(re.findall(r'href="prompts/([^"/]+)\.md"',readme))
 # Latest-prompts links also use href: distinguish the 100 actual visual tiles.
 showcased=set(re.findall(r'<img[^>]+>.*?href="prompts/([^"/]+)\.md"',readme.split('## Latest prompts')[0]))
 original_files={p.stem:p for p in (ROOT/'prompts').glob('*.md')}
 if len(videos)!=len(original_files): raise ValueError('Prompt-file/data count mismatch')
 refs=json.loads((ROOT/'data/references.json').read_text()) if (ROOT/'data/references.json').exists() else {}
 entries=[]
 for v in videos:
  slug=v['slug']; raw=original_files[slug].read_text();flags=[k for k,rx in CUES.items() if re.search(rx,v['prompt'],re.I)]
  # Read every original Markdown as well as every data prompt; retain the exact upstream files.
  if v['prompt'].strip() not in raw: raise ValueError('Data/Markdown text mismatch: '+slug)
  text=adapt(v,flags);p=ROOT/'prompts/gpt-6.1-high'/f'{slug}.md';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
  result_path=ROOT/'results'/slug/'result.json'
  result=json.loads(result_path.read_text().replace(str(ROOT), '$REPO')) if result_path.exists() else {'baseline':{'status':'not_generated'},'adapted':{'status':'not_generated'}}
  review_path=ROOT/'comparison/reviews'/f'{slug}.json'
  review=json.loads(review_path.read_text()) if review_path.exists() else {}
  entries.append({**v,'showcased':slug in showcased,'source_completeness':'partial' if v['prompt_partial'] else 'upstream_full',
   'dependency_cues':flags,'source_prompt_sha256':digest(v['prompt']),'source_file_sha256':digest(raw),
   'adapted_prompt_sha256':digest(text),'adapted_prompt':text,'reference':refs.get(slug,{}),'runs':result,
   'review_status':review.get('status','not_reviewed'),'review':review})
 audit={'upstream':UPSTREAM,'upstream_commit':(ROOT/'provenance/upstream.json').read_text() and json.loads((ROOT/'provenance/upstream.json').read_text())['commit'],
  'entries':len(entries),'original_prompt_files':len(original_files),'full':sum(not v['prompt_partial'] for v in videos),
  'partial':sum(v['prompt_partial'] for v in videos),'linked_remakes':sum(v['has_remake'] for v in videos),
  'readme_showcase':len(showcased),'categories':dict(collections.Counter(v['category'] for v in videos)),
  'dependency_cues':dict(collections.Counter(f for v in entries for f in v['dependency_cues'])),
  'prompt_audit':'All data prompts and Markdown files read and cross-checked by script. Dependency cues are heuristics; visual/reference review is not complete.',
  'unique_prompt_texts':len({v['prompt'] for v in videos}),
  'visual_reviewed':sum(v['review_status']=='reviewed' for v in entries),
  'model':MODEL,'reasoning_effort':'high'}
 dump(ROOT/'data/catalog.json',entries);dump(ROOT/'data/audit.json',audit)
 (ROOT/'docs/catalog.js').write_text('window.CATALOG = '+json.dumps(entries,ensure_ascii=False)+';\nwindow.AUDIT = '+json.dumps(audit,ensure_ascii=False)+';\n')
 (ROOT/'provenance/INVENTORY.md').write_text('# Source inventory\n\nPinned upstream: `'+audit['upstream_commit']+'`.\n\n'+ '\n'.join(f'- {k}: {v}' for k,v in audit.items() if k not in ['upstream_commit','upstream'])+'\n\nAll adaptations are draft instructions. No adaptation alone establishes generation or reference fidelity.\n')
 print(json.dumps(audit,indent=2))
if __name__=='__main__':build()
