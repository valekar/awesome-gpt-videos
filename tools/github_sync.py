#!/usr/bin/env python3
"""Use Git's configured GitHub credential without printing or persisting it."""
import argparse,fcntl,json,os,subprocess,urllib.request,urllib.error
from catalog import ROOT

def credential():
 env=dict(os.environ,GIT_TERMINAL_PROMPT='0')
 r=subprocess.run(['git','credential','fill'],input='protocol=https\nhost=github.com\n\n',capture_output=True,text=True,env=env,timeout=20,check=True)
 fields=dict(line.split('=',1) for line in r.stdout.splitlines() if '=' in line)
 value=fields.get('password')
 if not value:raise RuntimeError('No configured GitHub credential')
 return value

def api(path,method='GET',payload=None):
 token=credential()
 request=urllib.request.Request('https://api.github.com/'+path,method=method,data=json.dumps(payload).encode() if payload is not None else None,headers={'Authorization':'Bearer '+token,'Accept':'application/vnd.github+json','Content-Type':'application/json','User-Agent':'awesome-gpt-videos-publisher','X-GitHub-Api-Version':'2022-11-28'})
 with urllib.request.urlopen(request,timeout=30) as response:
  body=response.read();return json.loads(body) if body else {}

def repo():
 origin=subprocess.check_output(['git','remote','get-url','origin'],cwd=ROOT,text=True).strip()
 if not origin.startswith('https://github.com/'):raise RuntimeError('Expected a GitHub HTTPS origin')
 return origin.removeprefix('https://github.com/').removesuffix('.git')
if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--push',action='store_true');a=parser.parse_args();full=repo()
 if a.push:
  lock=ROOT/'work/github-push.lock';lock.parent.mkdir(exist_ok=True)
  with lock.open('w') as handle:
   fcntl.flock(handle,fcntl.LOCK_EX)
   local=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()
   subprocess.run(['git','push','origin',local+':refs/heads/main'],cwd=ROOT,env=dict(os.environ,GIT_TERMINAL_PROMPT='0'),check=True)
   remote=api('repos/'+full+'/commits/main')['sha']
   if local!=remote:
    comparison=api('repos/'+full+'/compare/'+local+'...'+remote)
    if comparison['status']!='ahead':raise RuntimeError('Pushed commit is not the remote head or its ancestor')
   print('Verified pushed commit:',local)
 runs=api('repos/'+full+'/actions/runs?per_page=3')['workflow_runs']
 print(json.dumps([{'id':r['id'],'status':r['status'],'conclusion':r['conclusion'],'url':r['html_url'],'commit':r['head_sha']} for r in runs],indent=2))
