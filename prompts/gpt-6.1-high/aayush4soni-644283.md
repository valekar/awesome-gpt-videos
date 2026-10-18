# GPT-6.1 high adaptation — aayush4soni-644283

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @aayush4soni. Source: https://x.com/aayush4soni/status/2104181266459644283
Reference page: https://skillry.dev/ai-videos/opus-5-5/aayush4soni-644283
Original prompt SHA-256: `076b4c2a00efadb9e3834f22226677141dc608d12fba7f4db0762179df510b43`.

## Source completeness

The upstream entry is marked partial: this may be a post or incomplete instructions. Treat it as partial evidence; never call an inferred reconstruction the original prompt.
Dependency cues found by automated text inspection: attachment_or_reference, native_renderer.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

Preserve geometry, materials, lighting, camera path, subject scale, scene density and physical interactions. Inspect near and far surfaces and important occlusions.

Upstream remake implementation tags (descriptive, not proof of the original stack): threejs, canvas. Use a fixed timestep or analytic scene state, seeded randomness, and a reproducible camera. Recompute Canvas state from time; reset transforms and compositing on every frame.

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
My family is planning to build a house, and all we had was the floor plan. I wanted to see how it would really look once it's built: which colors, layout and design would suit it best.

So I gave the plan to Claude Opus 5.5 and asked it to create a 3D view of the house.

It's one of the most useful things I've created recently. We can now walk through the house before a single brick is laid, and when we want to try a different color or layout, I just ask for the change.

In the video: the hall, room, and the terrace at dusk, all at eye height.

How it worked:

• I gave it the 5-page floor-plan PDF and one reference image for the front of the house.
• It read the drawings and rebuilt every floor: walls, doors, windows and stairs.
• Where a printed size didn't match the drawn wall, it flagged it (15 places) instead of quietly guessing.
• It furnished every room itself: 500+ pieces of furniture, decor and lighting.
• Everything runs in a web browser with three.js. No Blender, no game engine. You can walk through it like a game, in daylight or evening light, and the lamps actually light the rooms.
• It treated it like a real software project: ~37k lines of JavaScript, 185 unit tests, 56 browser tests, and deterministic video capture (render the same frame twice, get identical pixels).
• It even tracked down a bug of its own: a room's lighting changed depending on which room you walked in from.
• It split the work across sub-agents. Start to finish took about two days.

My part was the decisions: what each room is for, the style, and the changes I wanted.
</creator_material>
