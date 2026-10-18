#!/usr/bin/env python3
"""Stage a model response as a local HyperFrames project; preserve original model code."""
import argparse,json,pathlib,shutil,subprocess
from catalog import ROOT,dump,digest
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('slug');p.add_argument('--track',choices=['baseline','adapted'],required=True);a=p.parse_args()
 if not any(v['slug']==a.slug for v in json.loads((ROOT/'data/videos.json').read_text())):p.error('Unknown slug')
 source=ROOT/'results'/a.slug/a.track
 if not (source/'index.html').exists():p.error('No generated HTML source')
 metadata=json.loads((source/'metadata.json').read_text())
 current=json.loads((ROOT/'results'/a.slug/'result.json').read_text())[a.track]
 if current.get('status') not in ('generated','rendered','reviewed'):p.error('Current run has not completed source generation')
 if digest((source/'index.html').read_text())!=metadata.get('source_sha256'):p.error('Recorded model source hash mismatch')
 project=ROOT/'work/render-projects'/a.slug/a.track
 if not (project/'hyperframes.json').exists():
  subprocess.run([str(ROOT/'node_modules/.bin/hyperframes'),'init',str(project),'--non-interactive','--example=blank','--skill=general-video'],check=True,cwd=ROOT)
 metadata=json.loads((source/'metadata.json').read_text())
 shutil.copyfile(source/'index.html',project/'index.html')
 shutil.copyfile(ROOT/'node_modules/gsap/dist/gsap.min.js',project/'gsap.min.js')
 if (ROOT/'assets/fonts/Caveat.ttf').exists():shutil.copyfile(ROOT/'assets/fonts/Caveat.ttf',project/'Caveat.ttf')
 config=json.loads((project/'hyperframes.json').read_text());config.update(width=metadata['width'],height=metadata['height'],fps=30,duration=metadata['duration_seconds']);dump(project/'hyperframes.json',config)
 (project/'BRIEF.md').write_text(f'''---
workflow: general-video
flow: automation
storyboard: no
message: "Creator prompt comparison: {a.slug}"
length: {metadata['duration_seconds']}
aspect: "{metadata['width']}:{metadata['height']}"
---

Track: {a.track}. Target GPT-6.1 Sol/high. User requested generation and comparison for this collection. Preserve the recorded model source and disclose staging or repair changes. This stage bundles only local GSAP. Reference/evidence and provenance remain in the repository results and comparison folders. See comparison/METHODOLOGY.md. No new voice/music/assets are authorized by this staging step.
''')
 dump(project/'STAGING.json',{'source':f'results/{a.slug}/{a.track}/index.html','model_source_sha256':digest((source/'index.html').read_text()),'changes':['copied unchanged HTML','bundled gsap.min.js from gsap@3.14.2','made licensed Caveat font available; used by adaptation iteration 2'],'runtime':'hyperframes@0.8.171','track':a.track})
 print(project)
