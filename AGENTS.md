# Awesome GPT Videos

This repository adapts a pinned public prompt collection for GPT-6.1 Sol/high and records reproductions transparently.

- Preserve `prompts/*.md`, `data/videos.json`, upstream attribution and the upstream commit. They are historical evidence. New adaptations live in `prompts/gpt-6.1-high/`.
- Read `comparison/METHODOLOGY.md` before generation or evaluation. The local skill is `.agents/skills/awesome-gpt-videos/SKILL.md`.
- Model and effort are `gpt-6.1-sol` / `high`. Never silently substitute a model or relabel manually written output as a GPT-6.1 run.
- `python3 tools/catalog.py` rebuilds adaptations and the static gallery. Do not hand-edit generated catalog files.
- Preserve full durations, scenes and interactions. Mark missing reference/context explicitly. A partial post is not an identical-prompt baseline.
- A generated source file is not a rendered or visually reviewed result. Store actual logs, input, output, technical checks and matched-time review separately.
- Keep credentials, downloaded reference movies and raw execution logs out of public artifacts. Creator assets retain separate provenance.
- Run `python3 -m unittest discover -s tests` and `node --check docs/app.js` after pipeline changes. Inspect the gallery in a browser after UI changes.
- Publishing requires an authenticated GitHub account and a user-requested destination. Never push to `upstream`.
