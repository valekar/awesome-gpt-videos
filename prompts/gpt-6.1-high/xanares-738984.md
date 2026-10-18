# GPT-6.1 high adaptation — xanares-738984

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @Xanares. Source: https://x.com/Xanares/status/2105770390924738984
Reference page: None
Original prompt SHA-256: `a52148f68ffa4bf08d6d208ccd10aba1c452d3ab8cafa801b759906ff84a1e6d`.

## Source completeness

Upstream marks this as a full prompt. This does not establish that all referenced assets or prior chat context are available.
Dependency cues found by automated text inspection: none detected; manual reference review still required.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

Preserve geometry, materials, lighting, camera path, subject scale, scene density and physical interactions. Inspect near and far surfaces and important occlusions.

Upstream remake implementation tags (descriptive, not proof of the original stack): unspecified.

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
Make a 37-second demoscene tech demo for the track ~/Downloads/(filename).mp3.
The goal is graphics nobody has seen before. Like it's a statement for a new AI demoscene.

Story, in one continuous shot with no cuts:
- A chrome sphere floats in dark fog. On each hit in the track, it gains one Mandelbox fractal level.
- In the drop, the object grows until its top face is a landscape. Fly low over it at sunset, then dive off its edge.
- At the end, the fractal collapses into 3D gold letters of the title. Carve the letters from the same fractal and light them with the same light.

Look: path-traced quality. Soft shadows, ambient occlusion, glossy reflections, fog with light shafts, depth of field, motion blur, bloom.

Sync: analyse the track first. Save a JSON beat map with hits, breaks, and kick, snare and hat onsets. Kicks pulse the light. Hats add surface detail.

Tech:
- One WebGL2 fragment-shader raymarcher. One HTML page is both the live player and the render source.
- Live: 60 fps in Chrome.
- Offline: 1920x1080 at 60 fps with 16 samples per pixel. Render it in headless Chrome on the Mac GPU, pipe the PNG frames to ffmpeg, and use the MP3 as the audio.
- Do not use AI image or video generators.
- Check contact sheets of stills before the full render.
</creator_material>
