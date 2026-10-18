# GPT-6.1 high adaptation — twoclipping-762046

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @twoclipping. Source: https://x.com/twoclipping/status/2104674464868762046
Reference page: None
Original prompt SHA-256: `240e1ea5ba296f2bdb82686e887898ab6eeb61b5166c34d3c4492c6555aa013e`.

## Source completeness

Upstream marks this as a full prompt. This does not establish that all referenced assets or prior chat context are available.
Dependency cues found by automated text inspection: private_project_context, audio_dependency, input_request.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

Preserve geometry, materials, lighting, camera path, subject scale, scene density and physical interactions. Inspect near and far surfaces and important occlusions.

Upstream remake implementation tags (descriptive, not proof of the original stack): unspecified.

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
<inputs>
Ask me for: the one question a user asks my product and its one-line answer, two album covers, a royalty-free song around 110 BPM with a quiet intro and a hard drop (Mixkit, free for commercial use), and my logo for the ending. If I skip any, use the defaults: "is this all code?" / "yes. every frame.", two atmospheric photos, Mixkit "Head Bang".
</inputs>

<direction>
A 22 second square loop, 1440x1440 at 60fps, 2D only, one continuous take. Nothing ever cuts: every scene grows out of the last, and every gesture physically carries the camera into the next world. Every morph glides for 0.8s on cubic-bezier(.45,0,.15,1) and the camera zoom rides the same curve, so shapes change so smoothly you barely notice. Content dissolves in the back half of each glide. One gesture per scene.
Look: a warm light stage (#f3f3f0 to #e3e3de), black UI, the app world dark (#121212) tinted from the current album cover, one green accent (#1ed760). Geist for UI, the real macOS pointer, soft layered shadows that grow with the shape's height.
Banned: hard cuts, bouncy springs, particles, glows, zooming in and straight back out, holds longer than 1s, anything that looks like a template.
</direction>

<structure>
Beats are the song's, and the press lands on its drop.
Generate: the cursor clicks, the pill glides into a spinner, then a check.
Chat: the check splits into three typing dots (goo). The left dot flies up into the question bubble and types it, the right one flies down into the reply. Both contract back into dots while gliding in and pour into the middle one.
Play: the middle dot bends into a play triangle, point by point. The cursor presses it on the drop: a white button pops in under the click and the dark app floods out around it, so the leftover white becomes the play button. The camera pulls back to reveal the full now-playing screen: big cover, title, heart (liked, fills green), progress, controls, volume.
Swipe: the cursor drags the cover sideways, the next track slides in, and the whole app retints from the new cover.
Drag: the camera glides to the volume. The cursor drags it to max and keeps pulling: the bar rubber-bands and drags the camera sideways out of the app, tracking the knob across a dark dotted canvas.
Chart: the line lands and bends up into a green chart while the number counts up. The volume knob becomes its last point.
Dive: the cursor clicks that point and the camera dives into it until the light stage fills the frame.
Ending: an "Ask [my product]" button grows out of the light, thins into a line, and the line fans out into my logo (default: the Claude spark, six copies rotating into twelve rays in Claude orange). It folds back into the line, which thickens into Generate. Last frame = first frame.
</structure>
</creator_material>
