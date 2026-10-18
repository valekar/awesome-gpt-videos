#!/usr/bin/env python3
"""Attach a locally verified, newly rendered result to the static gallery."""
import argparse,json,pathlib,shutil,subprocess,sys
from catalog import ROOT,dump,digest
from generate import record
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('slug');p.add_argument('--track',choices=['baseline','adapted'],required=True);p.add_argument('--video',type=pathlib.Path,required=True);p.add_argument('--check',type=pathlib.Path,required=True);a=p.parse_args()
 original=json.loads((ROOT/'results'/a.slug/a.track/'metadata.json').read_text())
 check=json.loads(a.check.read_text())
 if check.get('ok') is not True or check.get('browserSkipped') is True:p.error('An actual passing HyperFrames browser check is required')
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_type,width,height,r_frame_rate','-of','json',str(a.video)],text=True))
 video=next(s for s in probe['streams'] if s['codec_type']=='video')
 if abs(float(probe['format']['duration'])-original['duration_seconds'])>0.1:p.error('Render duration differs from model source')
 if (video['width'],video['height'])!=(original['width'],original['height']):p.error('Render dimensions differ from recorded source')
 dst=ROOT/'docs/media'/a.slug/a.track;dst.mkdir(parents=True,exist_ok=True)
 shutil.copyfile(a.video,dst/'video.mp4')
 subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss','15','-i',str(dst/'video.mp4'),'-frames:v','1',str(dst/'poster.jpg')],check=True)
 # Only intentionally public model inputs/artifacts; execution diagnostics remain private.
 src=ROOT/'results'/a.slug/a.track
 for name in ['input.txt','response.json','index.html']:shutil.copyfile(src/name,dst/name)
 shutil.copyfile(ROOT/'node_modules/gsap/dist/gsap.min.js',dst/'gsap.min.js')
 if (ROOT/'assets/fonts/Caveat.ttf').exists():
  shutil.copyfile(ROOT/'assets/fonts/Caveat.ttf',dst/'Caveat.ttf');shutil.copyfile(ROOT/'assets/fonts/OFL.txt',dst/'FONT-LICENSE.txt')
 project=ROOT/'work/render-projects'/a.slug/a.track
 staged=(project/'index.html').read_text();shutil.copyfile(project/'index.html',dst/'render-source.html')
 original.update(status='rendered',reason='Rendered and technically checked. Matched-time visual review pending.',video_url=f'media/{a.slug}/{a.track}/video.mp4',poster_url=f'media/{a.slug}/{a.track}/poster.jpg',technical_check='passed',technical_check_limits='Canvas artwork has no DOM text boxes; automated text layout/contrast checks inspected zero text nodes. Visual review is required.',render_probe=probe,staged_source_sha256=digest(staged),source_modified_after_generation=digest(staged)!=original['source_sha256'])
 dump(src/'metadata.json',original);record(a.slug,a.track,original)
 public=json.loads(json.dumps(original).replace(str(ROOT),'$REPO'));dump(dst/'provenance.json',public)
 subprocess.run([sys.executable,str(ROOT/'tools/catalog.py')],check=True,cwd=ROOT,stdout=subprocess.DEVNULL)
 print(original['video_url'])
