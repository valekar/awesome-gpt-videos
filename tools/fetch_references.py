#!/usr/bin/env python3
"""Cache publicly reachable original movies with an explicit collection user agent."""
import concurrent.futures,json,pathlib,urllib.request,subprocess,datetime
from catalog import ROOT,dump

def fetch(v):
 slug=v['slug'];ref=v['reference'];p=ROOT/'work/references'/slug/'original.mp4';p.parent.mkdir(parents=True,exist_ok=True)
 try:
  if not p.exists():
   req=urllib.request.Request(ref['video_url'],headers={'User-Agent':'Awesome-GPT-Videos/0.1'})
   with urllib.request.urlopen(req,timeout=45) as r:
    if 'video/' not in r.headers.get('Content-Type',''):raise ValueError('Not video content')
    temp=p.with_suffix('.part')
    with temp.open('wb') as f:
     while block:=r.read(1024*1024):f.write(block)
    temp.replace(p)
  probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration:stream=codec_type,width,height,r_frame_rate','-of','json',str(p)],text=True,timeout=30))
  result={'slug':slug,'status':'downloaded','bytes':p.stat().st_size,'probe':probe,'source':ref['video_url']};dump(p.parent/'reference.json',result);return result
 except Exception as e:return {'slug':slug,'status':'fetch_failed','error':str(e)}
if __name__=='__main__':
 rows=[v for v in json.loads((ROOT/'data/catalog.json').read_text()) if v['reference'].get('video_url')]
 out={}
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  for result in pool.map(fetch,rows):
   out[result['slug']]=result
   if len(out)%25==0:print('reference cache',len(out),'/',len(rows),flush=True);dump(ROOT/'work/reference-cache.json',out)
 dump(ROOT/'work/reference-cache.json',out)
 print('finished',len(out),flush=True)
