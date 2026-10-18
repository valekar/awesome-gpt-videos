import copy,json,pathlib,sys,tempfile,unittest
from unittest.mock import patch
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
import catalog
import generate
from types import SimpleNamespace
from readme_comparisons import refresh
from adapted_queue import classify
class ComparisonTests(unittest.TestCase):
 def test_active_entry_cannot_overwrite_input_or_start_provider(self):
  with tempfile.TemporaryDirectory() as folder:
   root=pathlib.Path(folder);entry=root/'results/example';out=entry/'adapted';out.mkdir(parents=True)
   (entry/'result.json').write_text(json.dumps({'adapted':{'status':'running'}}));(out/'input.txt').write_text('preserved input')
   with patch.object(generate,'ROOT',root),patch.object(generate.subprocess,'run') as provider:
    with self.assertRaises(RuntimeError):generate.run_one({'slug':'example'},SimpleNamespace(track='adapted'))
    provider.assert_not_called()
   self.assertEqual((out/'input.txt').read_text(),'preserved input')
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
  v={'slug':'example','category':'motion','prompt':'Canvas promo','runs':{'adapted':{'status':'not_generated'}}}
  with tempfile.TemporaryDirectory() as folder:
   root=pathlib.Path(folder);p=root/'work/references/example/reference.json';p.parent.mkdir(parents=True)
   p.write_text(json.dumps({'status':'downloaded','probe':{'streams':[{'codec_type':'video'},{'codec_type':'audio'}]}}))
   with patch('adapted_queue.ROOT',root):self.assertEqual(classify(v),'audio_review_needed')
if __name__=='__main__':unittest.main()
