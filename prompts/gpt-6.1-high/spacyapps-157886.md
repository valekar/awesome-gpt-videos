# GPT-6.1 high adaptation — spacyapps-157886

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @SpacyApps. Source: https://x.com/SpacyApps/status/2105833401127157886
Reference page: https://skillry.dev/ai-videos/opus-5-5/spacyapps-157886
Original prompt SHA-256: `a51dc31e9501c872d3256e7a6d0328bd9b0fc1601894d964d177c4137ab372b0`.

## Source completeness

Upstream marks this as a full prompt. This does not establish that all referenced assets or prior chat context are available.
Dependency cues found by automated text inspection: none detected; manual reference review still required.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

Preserve controls, game mechanics, physics, progression and HUD. Deliver a playable version plus a deterministic replay for video comparison; a scripted movie alone does not satisfy this prompt.

Upstream remake implementation tags (descriptive, not proof of the original stack): threejs, shader, canvas. Use a fixed timestep or analytic scene state, seeded randomness, and a reproducible camera. Drive shader uniforms from deterministic timeline time and verify rendering on the target browser/GPU. Recompute Canvas state from time; reset transforms and compositing on every frame.

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
Build "Jelly Dice": a single self-contained HTML file (all JS/CSS inline, no build step) with translucent gummy-candy dice that behave like real soft bodies. Render with raw WebGPU (WGSL shaders, no three.js). If WebGPU is unavailable, show a clean fallback card that
</creator_material>
