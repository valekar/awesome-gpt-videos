# GPT-6.1 high adaptation — okapi-fukugyo-166351

Target model: `gpt-6.1-sol`; reasoning effort: `high`.
Track: adapted replication. Status: draft; not visually validated.
Creator: @okapi_fukugyo. Source: https://x.com/okapi_fukugyo/status/2103586082336166351
Reference page: None
Original prompt SHA-256: `3fcc01564cfe6c011c787f7d35d2914a61479c8384f2fcd63442b3d66fa56df4`.

## Source completeness

Upstream marks this as a full prompt. This does not establish that all referenced assets or prior chat context are available.
Dependency cues found by automated text inspection: audio_dependency.

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
次の3つを私に質問すること：図形が変身する8〜12個の画面部品（例：ボタン、読み込み中の表示、音楽プレーヤー、音量スライダー、オン/オフのスイッチ、タブ、グラフ、⌘Kで開く検索窓、一瞬出る通知）、色は完全な白黒か差し色1色か、そして120BPM（1分間に120拍のテンポ）前後の著作権フリーの曲（例：Mixkit、商用利用無料）。
</inputs>

<direction>
デザイナー向け作品サイト「Dribbble」に載るレベルの、洗練された画面の動き。図形は1つだけで、絶対に場面を切り替えない。すべての状態は、同じ1つの図形が大きさ・角の丸み・色を変えながら形を変えていく動きで表し、中身は短いぼかしをはさんで入れ替える。カーソルが本物のクリックとドラッグで、すべての変化を起こす。背景はあたたかみのある明るいグレー、部品は白と黒、画面の文字は日本語で、日本語フォントはNoto Sans JP、英数字と記号はGeist（1種類のフォント）。動きはすべて「ばね」のような自然な動きにし、行き過ぎ（跳ね返り）はごくわずかまで。カメラはズームして、各状態が画面いっぱいになるようにする。最後のフレームは最初のフレームと同じにして、ループさせる。
禁止：弾むような動き、粒が飛び散る演出、光るにじみ、部品へのグラデーション、線の太さが揃っていないアイコン、何も起きない無駄な間、テンプレっぽく見えるもの全般。
</direction>

<structure>
120BPM、7小節（約14秒）、毎拍なにかが起きる。
ボタン → 読み込み中の表示 → チェック → iPhoneのダイナミックアイランド風の表示 → 再生/一時停止のマークが滑らかに変わる音楽プレーヤー → 再生バーのつまみをドラッグして再生位置を動かす → 音量スライダーに変身（最大を超えてドラッグするとゴムのように伸びる） → オン/オフのスイッチが拍に合わせて切り替わる → スイッチのつまみが液体のように動くタブの選択表示になる → タブが開いて、自分で線を描いていくグラフに（カーソルを乗せると吹き出しが出る） → ⌘Kの検索窓に折りたたまれる → 入力して候補を絞り込む → Enter → 一瞬出る通知 → ボタンに戻る。
</structure>

<build>
1. HTMLファイル1つ、正方形1440x1440。すべての見た目は seek(t)（時間tを渡すと、その瞬間の画面が決まる関数）の中で、時間から計算する。CSSトランジション（自動アニメーション機能）もタイマーも使わず、フレーム間で状態を持ち越さない。
2. 「ばね」の動きは、式で直接求められる形（閉形式のステップ応答）にする。目標が何度も変わる値は、変化ごとに1つずつ計算した動きを足し合わせる。そうすれば、いつでも時間だけで値が決まる。
3. タブの選択表示は、左端と右端を別々のばねで動かし、進む方向の先端が後ろ側より先に伸びるようにする。スイッチのつまみも同じ手法。
4. ドラッグは直接操作：カーソルを押している間、値はカーソル位置から計算する。離したら、その位置からばねで戻る。
5. 曲はnumpy（計算用のツール）で解析して拍の位置を割り出し、小節の頭の拍から始める。操作音は、測定した音のピークの位置に置く。
6. Playwright（ブラウザを自動操作して画面を画像に書き出すツール）で描画する。1フレームあたり4コマ分を書き出して、ffmpeg（動画を作るツール）のtmixで重ねてモーションブラー（動きの残像）をかけ、60fpsにする。
7. 全編を書き出す前に、1拍ごとに1フレームだけ書き出して確認する。拍からズレているもの、窮屈なもの、読みにくいものを直す。
</build>

<gotchas>
カメラで拡大縮小される要素には will-change（ブラウザの描画設定）を絶対に付けない。付けると文字がぼやける。形が変わる箱の中で入れ替わる文字には、それぞれ専用の出入りのタイミングを持たせる（重なるのを防ぐ）。最後のフレームは、カーソルの位置と速度も含めて最初のフレームと完全に一致させる。そうしないと、ループがカクつく。
</gotchas>

<start>
まず入力内容を私に質問して、コードを書く前に、拍ごとの状態リストを見せて。
</start>
</creator_material>
