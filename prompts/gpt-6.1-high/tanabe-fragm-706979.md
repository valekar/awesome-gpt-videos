# GPT-6.1 high adaptation — tanabe-fragm-706979

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @tanabe_fragm. Source: https://x.com/tanabe_fragm/status/2103802156675706979
Reference page: None
Original prompt SHA-256: `e268508197186de78494311950770eba1baaf9b44a557244ee06c8a0591ef35b`.

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
# あなたの役割
あなたは一流の映像演出家（モーションデザイナー）です。
採用担当者が15秒見ただけで「この人に仕事を頼みたい」と思う、自己紹介用の映像を作ってください。
主役はあなた自身（Claude）です。

# 作るもの
- HTML・CSS・JavaScriptだけで完結する、1つのHTMLファイル
- 外部の画像や動画は使わない。図形・文字・粒子はすべてコードで描く（フォントはGoogle Fontsのみ可）
- 画面は16:9、1920×1080を基準にし、ウィンドウの大きさに合わせて縮小表示
- 長さはちょうど15秒。最後に「もう一度再生」ボタンを出す
- すべての動きを「経過時間」1本で管理し、requestAnimationFrameで60fpsで動かす
- 再生ボタンを押すと、Web Audio APIで合成した拍と効果音が動きにぴったり合って鳴る

# 進め方（この順で必ず行う）
1. 考え方を一文で決める（例：「1本の線が、あらゆる形に生まれ変わる」）
2. 色は3〜4色、書体は2種類までに絞り、理由を一行で書く
3. 0.5秒刻みの絵コンテを表で示す（時間／画面で起きること／使う技法／狙い）
4. 実装する
5. 下の「合格ライン」で自己点検し、足りない点を直してから出す

# 構成の目安
- 0〜2秒：つかみ。最初の0.5秒で目を奪う
- 2〜10秒：技の見せ場。1.5〜2秒ごとに違う技法へ切り替える
- 10〜13秒：最も密度の高い盛り上がり
- 13〜15秒：名前「Claude」がきれいに決まって終わる

# 必ず使う技法（最低6つ）
- 文字の動き（1文字ずつ登場、分解して組み直す）
- 図形の変形（丸が四角に、線が文字に、など）
- 切り抜き（マスク）を使った場面転換
- 奥行き（視差、立体的な回転）
- 粒子の集合と拡散
- 数字の数え上げや、線が描かれていく表現

# 合格ライン
- 等速の動きはゼロ。すべての動きに緩急をつける（入りは速く、止まりは柔らかく、ばねの揺れも使う）
- 場面をまたぐ動きは重ねる。前の動きが終わる前に次が始まり、切れ目を感じさせない
- 主要な動きは0.5秒ごとの拍（120BPM相当）にそろえる
- 見せ場の直前に0.3〜0.5秒の「溜め」を置き、強弱を作る
- どの瞬間で一時停止しても、1枚の絵として美しく成立する
- ありがちな表現は避ける（全部フェードイン、虹色の色使い、意味のない回転）

# 最後に
完成したファイルと、絵コンテの表を出してください。
説明は3行以内で十分です。
</creator_material>
