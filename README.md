# Awesome GPT Videos

A GPT-6.1 Sol / **high reasoning** adaptation and reproduction lab inspired by [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos). Original creator prompts, attribution and source metadata remain intact. GPT adaptations and measured results are kept separately.

**This is work in progress. The 703 prompts have been inventoried and adapted as drafts; they have not all been generated, rendered or visually validated.** Never interpret a draft prompt or a linked upstream remake as a successful GPT test.

## Collection

| Inventory | Count |
| --- | ---: |
| Creator entries / original Markdown files | 703 |
| Unique prompt texts | 684 |
| Upstream full prompts | 496 |
| Partial prompts / creator-post material | 207 |
| Reachable original-video endpoints (HEAD check) | 418 |
| README showcase videos | 100 |
| Motion / 3D / explainer / interactive entries | 369 / 117 / 116 / 101 |

Pinned upstream commit: `92aee2f586ac0715cb3cbcb6384834f98a33383d`, imported 2026-10-18. Counts and source checks are in [`data/audit.json`](data/audit.json), [`data/references.json`](data/references.json), and [`provenance/INVENTORY.md`](provenance/INVENTORY.md). “Full” means the upstream full-text label; it does not establish that referenced assets or prior conversation are available.

## Comparison gallery

The buildless, responsive gallery in [`docs/`](docs/) shows the original creator output beside the selected GPT track, with search, category/source/status filters, pagination, prompt copying, source links, and run provenance. Two available GPT tracks:

- **Original prompt**: verbatim published creator material, plus the common renderer/output contract.
- **Adapted replication**: GPT-specific production instructions plus a timed brief inferred from the reference and any declared reference images.

Each result has its own generation, render and review state. No winner or equivalence claim is assigned automatically. Upstream creator work and Skillry remakes are external references, not GPT results. Video playback depends on the original host; creator links remain available.

```sh
npm ci
npm run catalog
npm run preview
# Open http://127.0.0.1:4173
```

[`pages.yml`](.github/workflows/pages.yml) builds and deploys the gallery from `main`. Published repository: [valekar/awesome-gpt-videos](https://github.com/valekar/awesome-gpt-videos). The [comparison gallery](https://valekar.github.io/awesome-gpt-videos/) deploys through GitHub Actions. `origin` is the GPT repository; `upstream` remains the pinned inspiration source. Publishing uses the existing configured Git credential; a separate GitHub CLI login is not required.

## Prompts and generation

- [`prompts/`](prompts/) — 703 original files, unchanged.
- [`prompts/gpt-6.1-high/`](prompts/gpt-6.1-high/) — 703 draft adaptations, each preserving the creator material and its hash.
- [`comparison/METHODOLOGY.md`](comparison/METHODOLOGY.md) — controls, missing-context handling, reproduction and review.
- [`comparison/matched-briefs/`](comparison/matched-briefs/) — inferred timed reconstruction briefs.
- [`results/`](results/) — saved exact inputs, model responses, source and run metadata.
- [Repository skill](.agents/skills/awesome-gpt-videos/SKILL.md) — reusable generation and comparison workflow.

```sh
# Inspect a queue without spending model usage:
python3 tools/generate.py --showcase --track baseline

# Execute an entry with the signed-in local Codex account:
python3 tools/generate.py sarut0bisasuke-069973 --track baseline --execute

# Exact reproduction additionally needs a prepared timed reference brief:
python3 tools/generate.py <slug> --track adapted --execute

# Stage generated source for the host's HyperFrames check/preview/render workflow:
python3 tools/prepare_render.py <slug> --track adapted

npm test
```

The runner pins `gpt-6.1-sol` and `model_reasoning_effort="high"` through `@openai/codex@0.163.0`. It is resumable, serial, and stops on execution failure. Partial baseline sources and adapted entries without matched briefs become blocked with explicit reasons. It does not render or mark fidelity reviewed merely because generation succeeded. The local old Codex CLI rejected the model; the pinned newer CLI passed an authenticated model probe.

## Attribution

Original collection: **yihui-dev**, [upstream repository](https://github.com/yihui-dev/awesome-opus5-5-videos), MIT. Original prompts and videos belong to their linked creators. Keep the upstream [MIT license](LICENSE) and [original README](provenance/UPSTREAM_README.md). Separate media rights are not inferred from the code license. The comparison approach is informed by the local GPTcar reference-recreation workflow; its historical films and scene code are not reused as new GPT output. HyperFrames provides the rendering framework and GSAP provides timeline primitives. This is an independent collection, with no implied endorsement by OpenAI, Anthropic or Skillry.

## First recorded comparison

The first end-to-end case is **White Russian recipe** by [@Sarut0biSasuke](https://x.com/Sarut0biSasuke/status/2103418429248069973): 30 seconds, silent. The baseline selected a different layout and serving quantities; the adapted run uses an inferred reference brief and separately supplied reference frames. Adaptation iterations are preserved, including the corrected sidebar placement and subsequent drink-material refinements. This is a worked comparison. Current completion counts and pending states are reported in the live gallery and `data/audit.json`. Read the actual saved metadata and review notes for the current result.

The repository-local skill now explicitly requires full-resolution reference inspection before inferring layout from a contact sheet. It also separates missing assets, renderer differences, generated source, technical checks and sampled visual review.

## Continuing the corpus

`python3 tools/batch_generate.py --track baseline --workers 2 --research --execute` resumes ungenerated entries. Research mode is recorded separately from the code-only pilot. The queue stops on provider authentication/quota/model errors and never changes model.

`python3 tools/render_queue.py --watch` watches completed baseline sources, stages self-contained movies, runs actual browser checks, renders and verifies MP4s, and refreshes the local gallery. It leaves visual fidelity pending. External runtime assets and interactive controls require separate checks; their source is retained with a reason. Native renderer requests are routed separately. Downloaded reference movies and raw diagnostics remain local and ignored.

`python3 tools/github_sync.py --push` uses Git's configured credential helper and verifies the remote commit. Run tests and commit reviewed publication artifacts first. The generation/render workers update local state; a Git push is what updates the published Pages gallery.

`python3 tools/publish_progress.py --watch` publishes corpus run/render output changes to the configured `valekar/awesome-gpt-videos` destination after tests. It stops if the branch/destination changes or unrelated staged work exists. It does not assign visual acceptance.
