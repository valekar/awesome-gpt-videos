---
name: awesome-gpt-videos
description: Reproduce and compare entries from the Awesome GPT Videos creator-prompt collection with GPT-6.1 Sol at high reasoning. Use for this repository's original-prompt runs, reference reconstructions, prompt improvements and comparison gallery; not generic video creation.
---

Read `AGENTS.md` and `comparison/METHODOLOGY.md` from the repository root. Locate the requested entry by slug or prompt text in `data/catalog.json`. Its published material, GPT adaptation, partial/full label and dependency cues are separate evidence.

For a baseline, preserve the creator text and use `tools/generate.py --track baseline`; keep the common renderer contract visible in the saved input. Partial posts cannot establish an identical-original-prompt comparison. Missing assets or product context must be recorded, not invented.

For a recreation, inspect the complete original and its transition boundaries first. Inspect full-resolution frames before inferring left/right regions or subject scale from a tiled contact sheet. Write `comparison/matched-briefs/<slug>.md` with timed composition, geometry, material, camera, action, exact text and sound. Mark inferred choices and unavailable assets. Preserve runtime, language, subjects, brands, scene scope and interactions. Run `tools/generate.py --track adapted` with declared reference evidence. The target is `gpt-6.1-sol` / `high`; stop on unavailable access rather than changing model.

Use the creator's explicit renderer; otherwise follow the host's video workflow (HyperFrames in this workspace). `tools/prepare_render.py` stages generated HyperFrames source and local GSAP without overwriting the recorded model response. Render and technically verify with the owning workflow. Preserve input/response hashes and document any human or model repair as an additional iteration.

Compare decoded output/reference frames at matching times for every scene and transition. Record technical validity and fidelity separately in `comparison/reviews/`. Inspect values in motion before deciding a reference number is wrong. A successful encode is not visual parity. Interactive entries also require tested controls and a replay.

Publish only verified run metadata and user-owned or cleared result assets to `docs/`. Run `python3 tools/catalog.py` to refresh the gallery. Keep original files, attribution and the pinned upstream commit intact; do not relabel the source author's work or a prior model's film as a new GPT run.

When a source asks for public research, use the explicitly recorded research mode instead of declaring its assets unavailable because the code-only harness disabled browsing. Keep the two execution protocols distinguishable. Declared model frame analysis is useful for drafting a reconstruction; it does not establish audio coverage or full transition acceptance. Preserve its exact evidence timestamps and inspect critical full-resolution frames before improving source-specific prompts.

A reference-analysis response may separate scene samples and exact text from its prose brief. Include all these fields in the reconstruction input; never assume the prose alone includes the complete film. Explicitly list supplied local fonts in the generation contract. Verify that the saved HTML loads them and waits for font readiness before judging typography. At matched timestamps, check bottle exit, pour completion, liquid tint and progress-node scale; layout similarity alone misses these differences. A render worker may attach technically checked movies, but must leave fidelity pending and route interactive controls and external dependencies to their own checks.

For the adapted-first corpus run, use `tools/adapted_queue.py`. It records reference analysis, reference-guided generation, the owning technical render, decoded matched-time model comparison, and at most the declared revision budget. Native renderer, interactive replay, missing reference and unreviewed audio cases remain in `docs/adapted-queue.json` with their actual follow-up; prioritizing ready films does not complete these cases.

Read `comparison/prompt-improvements/<slug>.md` when present. These are scoped, attributed review-derived suggestions and are appended to regenerated adaptation prompts; they never replace the verbatim creator material. Preserve scene branding even when it names Claude/Opus. Preserve the decoded source frame rate as well as aspect and duration. Generate and review using all declared evidence sheets and full-resolution details. Do not erase old differences merely because a revision exists: compare the new MP4 again. Automated paired-frame reviews must name the model and sampling, and retain unresolved audio, transition and small-text uncertainty.

`tools/catalog.py` also regenerates the README comparison block. Keep paired reference/result previews, attempt counts, prompt/brief/review links and current differences in it. A sampled comparison and a technical render must remain distinct from full visual acceptance.

For typed or progressively revealed closing titles, include a decoded frame within the last0.05seconds in addition to the prior second. A partially revealed string at duration-minus-one is not the finished closing copy. The typography reconstruction exposed this: the original completes “Opus5.5” near the end while an early recreation held “Opu”. Compare the actual final tail before accepting text coverage.

For quantitative animations, compare the displayed integer separately from any fractional visual state. The token-bucket recreation matched the visible count yet initially omitted the partial next-token fill and green refill-slot accent. Preserve these state cues rather than “correcting” a reference display from an integer counter alone. Keep the per-case measured differences in its prompt-improvement record.
