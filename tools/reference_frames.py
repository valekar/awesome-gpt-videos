#!/usr/bin/env python3
"""Create timestamped evidence sheets and scene-change frames; these are not output artwork."""
import argparse,json,math,pathlib,re,subprocess
from PIL import Image,ImageDraw,ImageFont
from catalog import ROOT,dump

def prepare(slug):
 base=ROOT/'work/references'/slug;movie=base/'original.mp4'
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_type,width,height,r_frame_rate,duration,nb_frames','-of','json',str(movie)],text=True))
 vid=next(s for s in probe['streams'] if s['codec_type']=='video');duration=float(vid.get('duration') or probe['format']['duration']);folder=base/'evidence';folder.mkdir(exist_ok=True)
 # Exact decoded timestamps are extracted from showinfo after selection.
 selected=subprocess.run(['ffmpeg','-hide_banner','-y','-i',str(movie),'-vf',"select='isnan(prev_selected_t)+gte(t-prev_selected_t,1)',scale=480:-1,showinfo",'-fps_mode','vfr','-q:v','3',str(folder/'frame-%04d.jpg')],text=True,capture_output=True,check=True)
 times=[float(t) for t in re.findall(r'pts_time:([0-9.]+)',selected.stderr)]
 files=sorted(folder.glob('frame-*.jpg'));items=list(zip(files,times));sheets=[]
 for page in range(math.ceil(len(items)/16)):
  group=items[page*16:(page+1)*16];h=Image.open(group[0][0]).height;canvas=Image.new('RGB',(4*480,4*(h+26)),(30,30,30));draw=ImageDraw.Draw(canvas)
  for i,(path,t) in enumerate(group):
   x=i%4*480;y=i//4*(h+26);canvas.paste(Image.open(path),(x,y+26));draw.text((x+8,y+4),f'{t:.3f} s',fill='white')
  path=folder/f'sheet-{page+1:02d}.jpg';canvas.save(path,quality=88);sheets.append(path)
 # Preserve full-resolution reference frames for fine geometry and typography.
 full=[]
 for i,t in enumerate([min(1,duration/5),duration/2,max(0,duration-1),max(0,duration-.05)]):
  path=folder/f'full-{i+1}.jpg';subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss',str(t),'-i',str(movie),'-frames:v','1',str(path)],check=True);full.append(path)
 scene=subprocess.run(['ffmpeg','-hide_banner','-i',str(movie),'-vf',"select='gt(scene,0.18)',showinfo",'-fps_mode','vfr','-f','null','-'],text=True,capture_output=True,check=True)
 cuts=[float(t) for t in re.findall(r'pts_time:([0-9.]+)',scene.stderr)]
 meta={'slug':slug,'width':vid['width'],'height':vid['height'],'fps':vid['r_frame_rate'],'duration_seconds':duration,'audio_streams':sum(s['codec_type']=='audio' for s in probe['streams']),'sample_times':times,'scene_change_times':cuts,'sheets':[str(p.relative_to(ROOT)) for p in sheets],'full_frames':[str(p.relative_to(ROOT)) for p in full],'review_coverage':'Full duration sampled at >=1s spacing, scene-change timestamps detected. This is not a frame-by-frame review.'}
 dump(base/'evidence.json',meta);return meta
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('slug');a=p.parse_args();print(json.dumps(prepare(a.slug),indent=2))
