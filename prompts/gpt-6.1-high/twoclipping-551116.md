# GPT-6.1 high adaptation — twoclipping-551116

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @twoclipping. Source: https://x.com/twoclipping/status/2106101258834551116
Reference page: None
Original prompt SHA-256: `559f7579879fc254eaf10d64973bb5ad807369d1792e08b1c3542476f96f2a44`.

## Source completeness

Upstream marks this as a full prompt. This does not establish that all referenced assets or prior chat context are available.
Dependency cues found by automated text inspection: attachment_or_reference, private_project_context, audio_dependency, input_request.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

Preserve visual hierarchy, exact UI states, typography, beat grid, morph continuity and loop seam. Inspect all transition states as well as settled frames.

Upstream remake implementation tags (descriptive, not proof of the original stack): unspecified.

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
<inputs>
Ask me for: my product's name (one lowercase word), a 4-word tagline, the 3-step story of what it does, a launch date and domain, a royalty-free song with a clear drop, 4 vertical talking-to-camera clips and 12 portrait photos. If I skip any, use the defaults: "castr", "ugc ads, cast by ai", write a brief → scan 1,000 creators → cast 4, Mixkit "Cat Walk" (129.6 BPM, drop at 29.7s), free Pexels clips and portraits, and transparent stickers from Pixabay (serum, mic, megaphone, vintage camera, spotlight, lips).
</inputs>

<direction>
A 25 second square launch trailer, 1440x1440 at 60fps, loud poster style. Cobalt #2B3BFF, ink #0E0F1F, cream #F6E4C6, pink #FF7DC7, tangerine #FF5A1F. Archivo 900 extra-condensed for names, expanded for headlines, Geist and Geist Mono for labels. Op-art sunburst, scrolling waves, film grain. Real media only: the clips play inside the design, and the stickers get a white die-cut border and a soft shadow.
Motion rules: the camera never stops (a slow 1.03-1.07 push on every scene), nothing pops in (letters rise through a mask line one by one), nothing snaps to the beat (patterns rotate continuously), swaps are carousel glides of about 0.55s, colour changes fade over about 0.35s, stickers ease in and then keep a slow sway. No full stops after the wordmark or any headline.
Banned: beat-snapped rotations, pop-in slams, white flashes, crossfades between scenes, hard cuts, templates.
</direction>

<structure>
54 beats. The song starts 8 beats before its drop.
Beats 0-8: a cobalt sunburst turns around a breathing cream disc. The wordmark types in with a gliding caret and the tagline pill rises. The disc floods the frame into the drop.
Beat 8, the drop: the cream becomes the face of a 3D box and "ONE BRIEF" rises letter by letter. The camera pulls back to the box floating on waves. On beat 12 it turns to "1,000 CREATORS" (stacked, with outlined echoes), on beat 14 to "ZERO DMs".
Beats 16-22: a whip to a dark desk. A tangerine "BRIEF #042" ticket types its rows (product, vibe, cast, due), stickers drift on, a polaroid of a real clip drops onto the corner, and a "NOW CASTING" stamp presses down on beat 20.
Beats 22-34: the casting stage. A crowd of black and white portraits in an arc, a 3D stage block, and the creators gliding through like a carousel. Each plays live in a big disc in black and white, with their name in pink on the stage, their followers, and a MATCH % that counts up. One beat later a "CAST ✓" stamp lands and the clip fades to colour. A counter rolls 1/4 to 4/4.
Beats 34-39: pink floods out of the last disc. The disc morphs into a phone screen (the clip keeps playing) and fans into 4 phones playing all 4 creators, with views counting up. "4 ADS" and "BY FRIDAY" rise.
Beats 39-44, the music's break: the pink floor drops away and a cream "JOIN THE WAITLIST" ticket glides down onto the sunburst. On the pickup its stub tears off.
Beats 44-54: the ticket body morphs into a poster arch. The wordmark rises in, then the tagline, then an info bar slides up in 3 blocks (date, numbers, domain) and a ticker runs round the frame edge. Then it all folds back into the opening disc, so the last frame is the first.
</structure>

<build>
1. One HTML canvas. Every frame is a pure function of time inside seek(t).
2. A beat map in beats, B = 60/BPM, with the song placed so its drop lands on beat 8.
3. The 3D box is an orthographic projection: each face is a 1440px offscreen canvas drawn with an affine transform and shaded by its normal.
4. Cut the clips to 30fps JPEG sequences with ffmpeg, draw frame floor(t*30), and do the black and white with ctx.filter.
5. Trim the sticker PNGs and add the die-cut border by dilating their alpha.
6. Sound: a downloaded SFX for every event (a shutter on every cast, whooshes on the glides, key clicks on the typing), each placed by its measured peak. Loudnorm to -14 LUFS.
7. Render with Playwright at 60fps with 8 motion-blur subframes. Scan for single-frame pops, then compare its motion against a reference video (hard jumps per second, share of still frames).
</build>

<gotchas>
A pattern that rotates one notch per beat reads as stutter: rotate it continuously, and pick each ring's speed so it lands on the same pattern at the last frame. 4 subframes ghost on fast whips, so use 8. A layer whose background is a huge flood circle still covers the screen after sliding down one frame height, so switch it to a full-frame rect once it has flooded. Counters read the frame's time, not the subframe's. The disc must morph inside the same camera transform as the scene it leaves, or it jumps.
</gotchas>

<start>
Ask me for the inputs, then show me the beat map and 6 stills (open, box, brief, casting, phones, poster) before you render.
</start>
</creator_material>
