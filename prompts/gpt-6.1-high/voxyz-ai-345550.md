# GPT-6.1 high adaptation — voxyz-ai-345550

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @Voxyz_ai. Source: https://x.com/Voxyz_ai/status/2103117246860345550
Reference page: https://skillry.dev/ai-videos/opus-5-5/voxyz-ai-345550
Original prompt SHA-256: `ec7d4c8692e1aa758f17273227f9479e184844eafd2c41f946852a1ea7bdd71e`.

## Source completeness

The upstream entry is marked partial: this may be a post or incomplete instructions. Treat it as partial evidence; never call an inferred reconstruction the original prompt.
Dependency cues found by automated text inspection: attachment_or_reference.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

Preserve the complete explanatory sequence, language, narration, quantities, labels and causal demonstrations. Do not replace a mechanism with decorative text.

Upstream remake implementation tags (descriptive, not proof of the original stack): threejs, shader, canvas, gsap. Use a fixed timestep or analytic scene state, seeded randomness, and a reproducible camera. Drive shader uniforms from deterministic timeline time and verify rendering on the target browser/GPU. Recompute Canvas state from time; reset transforms and compositing on every frame. Use a paused seekable GSAP timeline; use explicit initial values and deterministic seeks.

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
I asked Opus 5.5 to explain gravitational lensing by building an interactive black hole lab

One prompt for the first version, then a dynamic workflow to polish it for three rounds while I slept. This is what I woke up to: 5h 28m end to end, $90 at API prices

https://blackhole.voxyz.ai

Drag the black hole and the sky behind it bends into arcs, closing into a full ring when everything lines up

Each round ran 3 agents. Two reviewers each picked 9 to 10 issues and ranked them P0, P1, P2. The third one fixed them.
Round 1: 3D materials and lighting + UI and type
Round 2: camera motion and interaction + science-communication design
Round 3: a design director deciding whether it ships + visual QA and performance

Every P0 got fixed, the rest only if worth it. When the two reviewers disagreed, it picked one and wrote down why. It backed up before each round, checked screenshots after, and rolled back anything it couldn't fix.
</creator_material>
