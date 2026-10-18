# Comparison method

The target is GPT-6.1 Sol (`gpt-6.1-sol`) with `high` reasoning. [Official model guidance](https://developers.openai.com/api/docs/guides/latest-model) confirms this model and effort. This is a reproduction collection, not a controlled Opus benchmark: upstream films were selected by their creators, with unknown model settings, hidden context, tools and iteration budgets.

## Three separate artifacts

1. **Published creator prompt**: exact text in `data/videos.json` and `prompts/<slug>.md`, hashed and attributed. Upstream labels 496 entries full and 207 partial. Full text can still rely on missing attachments or conversation history. There are 703 entries and 684 unique prompt texts.
2. **GPT adaptation**: `prompts/gpt-6.1-high/<slug>.md`. Generated category/technology-aware production instructions wrap the verbatim creator text. They are drafts, not individually validated reconstruction prompts. Keep on-screen brands and subjects even when their names mention the original model. Improve model instructions rather than rewriting the historical brief.
3. **Timed reconstruction brief**: `comparison/matched-briefs/<slug>.md`, inferred from the finished original. Inspect every scene, action and transition, preserve runtime/language/crop/audio, label inferences and missing evidence. A contact sheet alone is not a full transition audit. Preserve source availability and asset contributions.

## Two GPT tracks

- **baseline** supplies the unchanged creator material plus the common output/renderer contract. The contract is additional prompting, so this is not a literal reconstruction of the original agent environment. No reference frames or adapted brief are supplied. Missing required context blocks the run.
- **adapted** supplies the GPT adaptation, timed reconstruction brief and any declared reference images. It measures the effect of extra reference/production guidance as well as the model. A matched brief is required. Attached reference images are evidence and may not be reused as generated artwork.

Keep model, effort, output harness and sampling comparable. Record every prompt revision and iteration; do not cherry-pick and call it a single-shot result. Assets, reference images, fonts, shared render utilities, image/TTS models and human repairs must be declared. Never reuse original scene code or exported reference frames as the new film.

## Run states and acceptance

`not_generated` → `running` → `generated` → `rendered` → `reviewed`, with `blocked` and `failed` recorded separately. “Reviewed” means a review was performed; it does not imply an equivalence score or a pass. Keep baseline/adapted statuses independent. Record technical findings, visual findings and remaining limitations.

Before acceptance, compare decoded original and new MP4s at identical timestamps. Include every shot and transition boundary, not just midpoint posters. Check scope/scene coverage, subject geometry, materials and detail, exact text, values, camera/crop, motion and audio. A technical render pass or pixel similarity score is insufficient to establish artistic fidelity. Record duration, resolution, frame rate, shared assets and actual runtime environment. Interactive entries additionally need working controls and a deterministic replay; a video alone does not fulfill them.

## Reproduce locally

```sh
npm ci
python3 tools/catalog.py
python3 tools/generate.py --showcase --track baseline       # inspect queue, no usage
python3 tools/generate.py <slug> --track baseline --execute
python3 tools/generate.py <slug> --track adapted --image <reference-sheet.jpg> --execute
python3 tools/prepare_render.py <slug> --track adapted
```

Generation uses the signed-in local Codex CLI, pinned to `@openai/codex@0.163.0`; the installed 0.136.0 CLI failed to parse the current model catalog and rejected the target. The newer CLI's model/effort probe succeeded on 2026-10-18. No API key is required for that signed-in CLI path. Raw events/stderr are ignored by Git. The runner stops on a provider failure rather than automatically spending on retries. It never changes model or resets usage limits.

The batch runner is serial and resumable. `--all` selects every entry; `--showcase` selects the 100 actual README showcase tiles (not the 30 latest-prompt tiles). Partial baseline entries and unprepared reproduction entries become blocked with a reason. The runner does not pretend that blocked entries have been tested.

## Reference availability

`python3 tools/references.py` checks the original-video endpoints corresponding to the collection. HTTP HEAD availability is a link check, not playback or visual verification. On 2026-10-18, 418 endpoints responded with video content types and 285 did not. Some direct command-line GETs returned 403 although browser media download succeeded; playback remains subject to the host's policies. Keep creator/Skillry links visible as fallback. Do not republish their films without rights.

## Publication

The static comparison gallery is in `docs/`; it uses relative paths so GitHub project Pages works. `.github/workflows/pages.yml` builds and deploys it from `main` after Pages is configured to use GitHub Actions. Generation is local and is never run in Pages CI. Never publish unreviewed original media, credentials, raw stderr or private assets.

## Recorded pilot limits

The White Russian baseline and reproduction use a tool-free code-generation mode: the CLI was instructed not to invoke tools, and only model-message events were observed. The common output contract constrains the renderer and external assets; it is additional context beyond the creator prompt. Native-renderer mentions (for example Blender, Manim, Raylib or Remotion) require routing to their own workflow instead of forcing them through this HTML runner.

The reproduction's first reference brief misread the contact-sheet layout; the first output followed that mistake. Iteration 2 corrected the sidebar and supplied Caveat separately. Iteration 3 addresses visual liquid level, floating ice and cream movement from a full-resolution reference frame. These iterations, extra reference images and font assistance prevent treating the result as a single-shot comparison with the baseline. All attempts remain archived under `results/<slug>/<track>/iterations/`.

HyperFrames' runtime checks passed on the pilot. The artwork is Canvas: the automated layout/contrast audits checked zero DOM text nodes, and no motion sidecar assertions were supplied. Thus those checks do not certify text readability, within-Canvas geometry, physical realism or fidelity. A passing technical check can also include a nonfatal source-length warning.
