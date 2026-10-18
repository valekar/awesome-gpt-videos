"""Refresh a bounded README section from recorded result and review evidence."""
import re
START='<!-- COMPARISONS:START -->'
END='<!-- COMPARISONS:END -->'
BASE='https://valekar.github.io/awesome-gpt-videos/'
def cell(s):return re.sub(r'\s+',' ',str(s)).replace('|','\\|').strip()
def note(v):
 r=v.get('review',{});a=r.get('adapted',{})
 differences=a.get('remaining_differences',[]) or r.get('differences',[])
 if differences:
  x=differences[0];return cell(x.get('description',x.get('detail','')) if isinstance(x,dict) else x)
 return 'Render checked; matched-time comparison pending.'
def refresh(root,entries,audit):
 recreated=[v for v in entries if v['runs'].get('adapted',{}).get('video_url')]
 baselines=[v for v in entries if v['runs'].get('baseline',{}).get('video_url')]
 lines=[START,'## Comparisons and progress','',f"**Priority: adapted recreations with GPT-6.1 Sol / high.** {len(recreated)} adapted recreations rendered; {len(baselines)} original-prompt baselines rendered. {audit['sampled_reviews']} entries have sampled review notes; {audit['visual_reviewed']} have a full review recorded.",'','References, extra inputs, supplied assets and revisions are disclosed. Sampled reviews do not establish visual parity or a model ranking. The [live comparison gallery]('+BASE+') contains both tracks and their current evidence.','','### Adapted recreations','','| Case | Original creator output | GPT-6.1/high recreation | Recorded differences |','| --- | --- | --- | --- |']
 for v in recreated:
  slug=v['slug'];r=v['runs']['adapted'];name=cell(v['author']+' · '+slug)
  original=f"[![Original by @{v['author']}]({v['poster_url']})]({v['reference'].get('video_url') or v['post_url']})" if v.get('poster_url') else f"[Original]({v['post_url']})"
  gpt=f"[![GPT recreation](docs/{r['poster_url']})]({BASE}#{slug})"
  review=f"[Review](comparison/reviews/{slug}.json)" if v['review_status']!='not_reviewed' else 'Review pending'
  brief=f"[Adapted prompt](prompts/gpt-6.1-high/{slug}.md) · [timed brief](comparison/matched-briefs/{slug}.md)"
  lines.append(f'| {name}<br>{brief} | {original} | {gpt}<br>{r.get("iteration",1)} recorded attempt(s) · {review} | {note(v)} |')
 lines+=['','<details>','<summary>Rendered original-prompt baselines</summary>','','These use the published creator material plus the common renderer contract. A rendered baseline is not a reference-guided recreation.','','| Creator / case | Result | Fidelity evidence |','| --- | --- | --- |']
 for v in baselines:
  label=cell(v['author']+' · '+v['slug']);slug=v['slug']
  review=f'[sampled notes](comparison/reviews/{slug}.json)' if v['review_status']=='sampled' else 'not compared yet'
  lines.append(f'| {label} | [Original and GPT baseline]({BASE}#{slug}) | {review} |')
 lines+=['','</details>','',END]
 block='\n'.join(lines);path=root/'README.md';text=path.read_text()
 if START in text:
  if END not in text:raise ValueError('Missing README comparison end marker')
  text=text[:text.index(START)]+block+text[text.index(END)+len(END):]
 else:text=text.replace('## Collection',block+'\n\n## Collection',1)
 if text!=path.read_text():path.write_text(text)
