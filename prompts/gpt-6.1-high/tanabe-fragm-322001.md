# GPT-6.1 high adaptation — tanabe-fragm-322001

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @tanabe_fragm. Source: https://x.com/tanabe_fragm/status/2107644501372322001
Reference page: None
Original prompt SHA-256: `83db48384308383eadc1695ee91252907dd0891bf02ac477db925bbba9b59eb3`.

## Source completeness

Upstream marks this as a full prompt. This does not establish that all referenced assets or prior chat context are available.
Dependency cues found by automated text inspection: attachment_or_reference.

## GPT task

Recreate the intent and complete scope of the creator material quoted below. Preserve subjects, brands, language, exact text, quantities, runtime, aspect ratio, scene order and requested interactions. A model name mentioned as the authoring tool does not change the requested on-screen content. Do not replace Claude/Opus branding when it is part of the actual scene.

Before an exact reproduction, inspect the original film across every scene and transition, and write a timed reconstruction brief with composition, camera, materials, motion, text and sound. Label every inferred choice. When an essential attachment, product, song, private directory or prior conversation is missing, record the missing input and stop that reproduction; do not invent it and claim a match.

Preserve geometry, materials, lighting, camera path, subject scale, scene density and physical interactions. Inspect near and far surfaces and important occlusions.

Upstream remake implementation tags (descriptive, not proof of the original stack): unspecified.

Use the creator's explicit renderer when specified. Otherwise use the host's video workflow (HyperFrames where available). Keep rendering infrastructure identical between benchmark tracks wherever possible. Use local, credited dependencies and record external asset/tool contributions. Make the result seekable for matched-time inspection; never substitute reference scene code, exported frames or the original movie for newly generated scene assembly.

Deliver editable source, the exact model input, model/effort/CLI metadata, dependency and asset ledger, rendered MP4 and poster, and a review record. Check subject coverage, timing, geometry/materials, typography, camera, motion and audio at matching decoded timestamps. Report technical validity and visual fidelity separately. Do not assign a pass or score before actual reference review.

## Creator material — verbatim

<creator_material>
添付の画像を「最後の画面」にして、全部タイルでできた30秒の広告動画（音つき・mp4）を作ってください。
ブラウザ（Three.js）で組み、Chromeで全コマを書き出し、ffmpegでmp4にします。

# ゴール
- 見る人は25秒、タイルの制作動画だと思って見る。最後の数秒で、添付画像（広告）だったと気づく
- 最後の画面は添付画像とほぼ同じ。文字が読める。画面いっぱいがタイル（床は見せない）

# 仕様
- 1920×1080、30fps、30秒。HTML1ファイル（Three.js。npmで入れてesbuildで1ファイルに固める）
- 時刻 t を渡すと、同じ t なら必ず同じ絵になる作りにする（seek(t)）
- タイルは1枚ずつ別のインスタンス。16:9の格子で約19万枚（576×324）
- 位置・向き・厚み・面取り・色を1枚ずつ変える。目地（隙間）は空き。線は引かない
- 添付画像は、タイルの色を取るためだけに使う（テクスチャとして貼らない）
- 素材は約12種（釉薬セラミック、スレート、真珠貝、白磁、テラコッタ、ガラスなど）。色の明るさと彩度で割り当てる
- 光は、左上の硬い太陽1つ。床は漆喰。奥に赤い大工のチョーク線がピンぼけで入る
- 被写界深度（円形ボケ）を後処理で自作する。しぼりは最初大きく、最後は小さく

# 流れ（秒）
0〜3　 床に暗いタイルが1枚。カメラは床すれすれ
3〜10　[組み始める場所]から、タイルが渦を巻いて落ちる。最初の1枚→周りの順に増える
10〜21 一気に外へ広がる。カメラが引いて[見せたい絵]が見えてくる
21〜24 全体が見える。文字になる場所は、周りと同じ淡い色のまま
24〜26 文字・ロゴ・ボタンのタイルが、左から順にパタパタ裏返って現れる
26〜30 真上からの構図で止まる。カーソルが[ボタンの文言]をクリックし、ボタンのタイルが少し沈む

# ハマりどころ（必ず守る）
- 文字になるタイルは、最初は周りの背景色で組む。背景色は、外側から内側へ塗り広げて決める。文字のふち（白ぶち）も一緒に裏返す。守らないと、途中で文字の形が見えてしまう
- 真上のカメラは、位置を真上ぴったりにしない（向きが90°回る）。止める所は、動きの勢いをゼロにする（補間のはみ出しで反転する）
- 最後の画面は、元画像と並べて色を比べ、露出・彩度・色味を合わせる
- 文字が小さくて読めないときは、タイル数を増やす
- 下地の暗い面は、タイルが着地したマスだけに出す

# 音
- ElevenLabsの効果音で、タイルを置く音・裏返す音・マウスのクリックを作る（各0.5秒）。作る前に、クレジットの消費を知らせる
- タイルの着地・裏返しの時刻に合わせて並べて重ねる。カメラが遠いほど小さく、数が増えたら雨のようにまとめる
- 24〜26秒のパタパタを、いちばん目立たせる。音量は -16 LUFS

# 進め方
1. 先に脚本（秒ごとの情景）を日本語で出し、OKをもらってから作る
2. 途中のコマ（最初のタイル／組み始め／引き／全景／文字が出る瞬間／最後）を自分で見て直す
3. 書き出しは Chrome（puppeteer-core）で seek(t) を30fpsぶん呼び、png を ffmpeg に流す
4. 納品は mp4（高画質と共有用）と、確認した画像

# 入力
- エンドフレーム: [添付]
- 組み始める場所: [例：人物の目]
- 引いたときに見せたい絵: [例：笑顔の女性]
- ボタンの文言: [例：無料体験はこちら]
</creator_material>
