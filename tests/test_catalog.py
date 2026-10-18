import hashlib,json,pathlib,sys,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'tools'))
from catalog import adapt,digest
from generate import make_input
class ProvenanceTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.original=json.loads((ROOT/'data/videos.json').read_text());cls.entries=json.loads((ROOT/'data/catalog.json').read_text());cls.audit=json.loads((ROOT/'data/audit.json').read_text())
 def test_complete_one_to_one_mapping(self):
  self.assertEqual(len(self.entries),703);self.assertEqual(len({v['slug'] for v in self.entries}),703)
  self.assertEqual({v['slug'] for v in self.original},{v['slug'] for v in self.entries})
  self.assertEqual(len(list((ROOT/'prompts/gpt-6.1-high').glob('*.md'))),703)
 def test_verbatim_source_and_hashes(self):
  for o,v in zip(self.original,self.entries):
   self.assertEqual(o['prompt'],v['prompt']);self.assertEqual(digest(o['prompt']),v['source_prompt_sha256'])
   self.assertIn(o['prompt'],v['adapted_prompt']);self.assertEqual(o['prompt_partial'],v['prompt_partial'])
 def test_partial_and_showcase_totals(self):
  self.assertEqual(sum(v['prompt_partial'] for v in self.entries),207)
  self.assertEqual(sum(v['showcased'] for v in self.entries),100)
  self.assertEqual(self.audit['unique_prompt_texts'],684)
 def test_baseline_never_receives_reconstruction(self):
  v=self.entries[0];s=make_input(v,'baseline')
  self.assertIn(v['prompt'],s);self.assertNotIn('TIMED RECONSTRUCTION BRIEF',s)
  self.assertNotIn('# GPT-6.1 high adaptation',s)
 def test_adapted_input_preserves_brief_and_original(self):
  v=self.entries[0];s=make_input(v,'adapted','TEST REFERENCE BRIEF')
  self.assertIn(v['prompt'],s);self.assertIn('TEST REFERENCE BRIEF',s)
 def test_sources_cannot_be_relabeled_as_results(self):
  for v in self.entries:
   for r in v['runs'].values():
    if r['status'] in ('generated','rendered','reviewed'):
     self.assertEqual(r['model'],'gpt-6.1-sol');self.assertEqual(r['reasoning_effort'],'high');self.assertTrue(r.get('input_sha256'));self.assertTrue(r.get('source_sha256'))
     if r['status'] in ('rendered','reviewed'):self.assertTrue(r.get('video_url'))
 def test_partial_warning_is_preserved(self):
  v=next(v for v in self.original if v['prompt_partial'])
  self.assertIn('partial',adapt(v,[]))
 def test_adaptation_does_not_rewrite_on_screen_model_brands(self):
  v=next(v for v in self.original if 'Opus 5.5' in v['prompt'])
  self.assertIn(v['prompt'],adapt(v,[]))
if __name__=='__main__':unittest.main()
