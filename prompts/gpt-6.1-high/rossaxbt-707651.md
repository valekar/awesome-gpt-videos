# GPT-6.1 high adaptation — rossaxbt-707651

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @rossaxbt. Source: https://x.com/rossaxbt/status/2107121188027707651
Reference page: None
Original prompt SHA-256: `4f950bd173fb86a58b6ce29889b1877ab461fb46ff384382e8a62294f09eadfd`.

## Source completeness

Upstream marks this as a full prompt. This does not establish that all referenced assets or prior chat context are available.
Dependency cues found by automated text inspection: attachment_or_reference, input_request.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

Preserve controls, game mechanics, physics, progression and HUD. Deliver a playable version plus a deterministic replay for video comparison; a scripted movie alone does not satisfy this prompt.

Upstream remake implementation tags (descriptive, not proof of the original stack): unspecified.

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
<inputs>
Ask me for: a short label for the opening toggle, one hero word, a percentage for the graph, the text for the final card, one accent color, and a track with a clear beat.
</inputs>

<direction>
A 2D motion design film in 16:9. Use a warm off-white canvas, near-black backgrounds, bold typography and one vivid orange accent. The orange dot connects every scene: it starts in the UI, becomes the dot over a letter, traces a spring graph, grows into a shape and returns on the end card. A cursor makes the opening click feel real. Keep the motion sharp and controlled, with small spring overshoots and no dead time.
Banned: stock footage, gradients, glows, particle bursts, random transitions and motion that isn't connected to an element already on screen.
</direction>

<structure>
Around 15 seconds, with a visual change on every major beat.
Open: a cursor clicks the orange toggle beside "Reduce Motion". The letters bend and move into place until only "Motion" remains, with the orange dot above the "i".
Spring: the dot jumps away from the word and lands on a graph. Its path draws a spring response, overshoots the target and settles beside a "+22%" callout.
Shape: the dot shoots across a line, grows into an orange circle and fills the frame. A black rounded square rotates inside it, then stretches into a pill. The scene contracts to a single orange dot on black.
Type: words like "SPRINGS", "EASING", "KINETIC TYPE", "3D" and "SOUND" orbit the dot. The circle of type opens out into a field of tiny dots.
Reveal: the halftone field expands and flips to black, revealing the final card: "Opus 5.5", "Motion designer." and "0 keyframes".
Return: the orange dot moves back through the halftone, graph and toggle. Match the final frame to the first so the video loops cleanly.
</structure>

<build>
1. One HTML file, 1920x1080 at 60fps. Compute every visual from time inside seek(t): no CSS transitions, timers or state carried between frames.
2. Use closed-form springs for the toggle, bouncing dot and graph. Draw the graph from the same spring function that moves the dot.
3. Animate letters individually for the "Reduce Motion" to "Motion" transformation. Keep the orange dot attached to the "i" until it begins its jump.
4. Make the orange circle, rotating square and pill different states of the same shape. Preserve its position and motion through each transformation.
5. Place the orbiting words along a circular path, then move their letters outward to hand the frame over to the halftone grid.
6. Draw the halftone as a grid of dots whose sizes respond to the orange dot. Let it grow past the frame edges before revealing the end card.
7. Sync the click, dot landing, graph peak, shape changes and final title to measured beats.
</creator_material>
