# GPT-6.1 high adaptation — demitiyageekzen-818523

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @DemitiyaGeekzen. Source: https://x.com/DemitiyaGeekzen/status/2103517910274818523
Reference page: https://skillry.dev/ai-videos/opus-5-5/demitiyageekzen-818523
Original prompt SHA-256: `0b2dea742cc542966afe6ad28a8f93a4c8fda589e67342554324c51af1e15dca`.

## Source completeness

The upstream entry is marked partial: this may be a post or incomplete instructions. Treat it as partial evidence; never call an inferred reconstruction the original prompt.
Dependency cues found by automated text inspection: none detected; manual reference review still required.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

Preserve geometry, materials, lighting, camera path, subject scale, scene density and physical interactions. Inspect near and far surfaces and important occlusions.

Upstream remake implementation tags (descriptive, not proof of the original stack): shader, webgl, canvas, audio. Drive shader uniforms from deterministic timeline time and verify rendering on the target browser/GPU. Record renderer, GPU and shader dependencies; verify output in the rendering browser. Recompute Canvas state from time; reset transforms and compositing on every frame. Preserve required audio and measure cue timing; do not silently output a silent version.

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
opus5.5有点强，我让它自由选题做交互页面和视频，
提示词：用你最强的思维和能力，根据对我的了解，自行寻找我可能喜欢的主题，制作一个30s的视频还有互动html，尽可能的展示你的前端能力！
它的选题思路：滕王阁·中秋夜。 今天（2026-09-25）正好是丙午年八月十五。所以我选了《滕王阁序》里最有画面感的那句："落霞与孤鹜齐飞，秋水共长天一色"。短片是船上视角：落日时一只孤鹜飞过太阳，天上是鱼鳞云，然后江天一色，楼阁由下往上亮起灯，满月从东边升起，江面上漂着河灯，诗句以竖排书法字幕配印章出现。

前端做的更牛，但是这里没法放！
画面：整幅画面由一个 WebGL2 着色器逐像素算出来，没有用任何图片。包括天空的暮色层次、按南昌纬度推算的日月轨迹、程序生成的鱼鳞云、9 组波浪叠加的江面倒影，以及用 Canvas 2D 画出来的滕王阁立面。
声音：全部用 WebAudio 实时合成，没有一段录音。古筝用 Karplus-Strong 弦振动模型，带按滑和揉弦；另有箫、江水声、虫鸣和混响。
自由观赏模式：可以拖动环视和缩放，拖时间轴改变时辰；点江面放河灯，会弹出一句诗、响一声古筝；点月亮进入月面特写；还能切换查看渲染图层，或者在网页里直接录制视频。
</creator_material>
