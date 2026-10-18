import copy,json,pathlib,sys,tempfile,unittest
from unittest.mock import patch
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
import catalog
from readme_comparisons import refresh
from adapted_queue import classify
class ComparisonTests(unittest.TestCase):
 def test_review_guidance_preserves_original_prompt(self):
  v=json.loads((ROOT/'data/videos.json').read_text())[0]
  with tempfile.TemporaryDirectory() as folder:
   root=pathlib.Path(folder);p=root/'comparison/prompt-improvements'/f"{v['slug']}.md";p.parent.mkdir(parents=True);p.write_text('At2.0s preserve the original brand and exact layout.')
   with patch.object(catalog,'ROOT',root):result=catalog.adapt(v,[])
  self.assertIn(v['prompt'],result);self.assertIn('At2.0s',result);self.assertIn(catalog.digest(v['prompt']),result)
 def test_readme_baseline_is_not_recreated_result(self):
  rows=json.loads((ROOT/'data/catalog.json').read_text());v=copy.deepcopy(next(v for v in rows if v['runs']['baseline'].get('video_url')));v['runs']['adapted']={'status':'not_generated'}
  with tempfile.TemporaryDirectory() as folder:
   root=pathlib.Path(folder);p=root/'README.md';p.write_text('# Demo\n\n## Collection\n\nKeep this prose.\n')
   refresh(root,[v],{'sampled_reviews':0,'visual_reviewed':0});first=p.read_text();refresh(root,[v],{'sampled_reviews':0,'visual_reviewed':0})
   self.assertEqual(first,p.read_text());self.assertIn('0 adapted recreations rendered; 1 original-prompt baselines rendered',first);self.assertIn('Keep this prose.',first)
 def test_audio_case_keeps_followup_instead_of_silent_recreation(self):
  v=next(v for v in json.loads((ROOT/'data/catalog.json').read_text()) if v['slug']=='deedydas-252537')
  self.assertEqual(classify(v),'audio_review_needed')
if __name__=='__main__':unittest.main()
