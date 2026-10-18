# GPT-6.1 high adaptation — pluvio9yte-662953

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @Pluvio9yte. Source: https://x.com/Pluvio9yte/status/2107087191738662953
Reference page: None
Original prompt SHA-256: `a13ea604010d99301f06c7291213f72a9db7aaaff686f8ec869d3191604a4f96`.

## Source completeness

Upstream marks this as a full prompt. This does not establish that all referenced assets or prior chat context are available.
Dependency cues found by automated text inspection: none detected; manual reference review still required.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

Preserve visual hierarchy, exact UI states, typography, beat grid, morph continuity and loop seam. Inspect all transition states as well as settled frames.

Upstream remake implementation tags (descriptive, not proof of the original stack): unspecified.

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
公开我的制作方案，发给Opus5.5就能用

  1. 选素材

  三个标准，直接决定成败：

  - 主体完整：人物或物体全身入画。细节会在加工中丢失，观众靠轮廓认东西，特写会变成一团。
  - 背景干净：纯色、雪地、天空都行，主体和背景容易分开。
  - 有明确的动作瞬间：打击、起跳、落地、转身。这些是后面做特效的支点。

  来源可以是自己拍的、视频模型生成的，或有授权的现成片段。

  2. 拆素材

  从每一帧提取三类信息：

  - 颜色：原画面。
  - 远近：每个位置离镜头多远，用现成的深度估计模型算。
  - 主体范围：哪里是主体、哪里是背景。

  另外找出镜头切换发生在哪些时刻。这一步的要点是保持稳定：远近和主体范围要在同一个镜头内统一处理，否则播放起来会抖。

  3. 定"粒子"和"样式"

  先决定用什么东西来重建画面：圆点、方块、文字、线条都可以。

  然后设计几种样式。每种样式其实只是三条规则的不同组合：

  - 放在哪：整个画面都放，还是只放在主体上。
  - 多大：统一大小，还是跟着明暗、远近变化。
  - 什么颜色：用原画的颜色，还是统一用一两种颜色。

  再加一个开关：是平铺在一个面上，还是按远近推进三维空间。推进去之后镜头才能环绕。

  准备四到六种差异明显的样式就够用。粒子的疏密需要自己看着调：太大认不出内容，太小又和原片没区别。

  4. 找节奏

  - 定速度：选定音乐的速度，把时间切成等长的小格。让一格正好是整数帧，后面所有切换都好对齐。
  - 找动作瞬间：结合"声音突然变响"和"画面突然变动"两个信号，找出素材里的打击点。
  - 准备音乐：可以用现成的曲子并分析出它的拍子，也可以按定好的速度合成一段，并在打击点上加重音。

  5. 编排

  做一张时间表，写明每一格用哪种样式、什么配色、镜头在哪。这张表单独存放，以后调节奏只改它。

  编排的四条原则：

  - 开头交代变化：先给原画面，再过渡到粒子，让观众看懂发生了什么。
  - 快慢交替：一直快会麻木，中间要有一段明显慢下来的部分。
  - 配色要撞：相邻两格的颜色和样式反差越大，切换越有力。
  - 结尾要有收束：比如粒子越来越大直到变成色块，或者回到原画面。

  6. 关键时刻的反馈

  在打击点上叠加短促的反应，按轻重分级：

  - 每一次都有的轻反馈：粒子变形一下、镜头顶一下。
  - 较重时才有的中反馈：一部分粒子朝镜头弹开。
  - 最重的一两次才用的大反馈：时间静止，镜头环绕。

  原则是弱而短。只动一部分粒子，几帧内结束，否则画面炸成一片，观众就看不清主体在做什么了。

  贯穿全程的工作方法

  - 先小样后全片：每做完一个环节，先渲染几帧看效果，确认了再往下。全片只在最后渲染。
  - 拿不准的参数一次出一排：比如疏密，让 AI 同时出五六个档位并排放，你来挑。
  - 改哪里渲哪里：调整某一段时只重新渲染那一段。
  - 让 AI 自己看图：每一步都要求它把渲染结果打开看一遍再汇报。
  - 所有随机都固定：保证同样的设置每次渲染结果一致，否则没法逐步修改。
</creator_material>
