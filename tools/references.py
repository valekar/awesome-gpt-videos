#!/usr/bin/env python3
"""Verify public original-video endpoints; never count a URL check as visual review."""
import concurrent.futures,json,pathlib,urllib.request,datetime
ROOT=pathlib.Path(__file__).resolve().parents[1]
def check(v):
 url=f"https://media.skillry.dev/opus-5-5/{v['slug']}/original.mp4"
 try:
  req=urllib.request.Request(url,method='HEAD',headers={'User-Agent':'Awesome-GPT-Videos/0.1'})
  with urllib.request.urlopen(req,timeout=18) as r:
   kind=r.headers.get('Content-Type','');status=r.status
  return v['slug'], {'status':'reachable' if status==200 and 'video/' in kind else 'unverified','video_url':url if status==200 and 'video/' in kind else None,'http_status':status,'content_type':kind,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'visual_review':'not_reviewed'}
 except Exception as e:return v['slug'],{'status':'unavailable','video_url':None,'error':str(e),'visual_review':'not_reviewed'}
if __name__=='__main__':
 videos=json.loads((ROOT/'data/videos.json').read_text())
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: rows=dict(pool.map(check,videos))
 (ROOT/'data/references.json').write_text(json.dumps(rows,indent=2)+'\n')
 from collections import Counter
 print(Counter(v['status'] for v in rows.values()))
