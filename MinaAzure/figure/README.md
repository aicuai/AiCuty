# Mina Azure — 公式フィギュアのターンテーブル（MiniMax H3）

## seed 1001（誕生日）

| | |
|---|---|
| ファイル | `turntable-1001.mp4`（704×704・124 フレーム・24fps・5.2 秒・灰背景）／ `turntable-1001.gif`（プレビュー） |
| 参照 | `img/figure/mina.png`（このリポジトリの公式フィギュア風レンダー） |
| モデル | MiniMax-H3 Ref2VA（pruned_int8_convrot）20 step、ComfyUI 標準ノード、RTX 4000 Ada 20GB × 1、5.4 分 |
| 検査 | 正面→右→背中→左→正面の 1 回転。最初と最後のフレームの差 2.5/255（ループが閉じる）。背中で長めに止まる |

### プロンプト（H3-Context-IR）

```
subject_definitions:
<Subject 1> is a collectible figure of Mina Azure (a chibi girl with very long straight icy sky-blue hair and evenly cut bangs, thin silver round glasses, aqua-blue eyes, an icy sky-blue beret with a navy ribbon, an icy sky-blue school-uniform idol dress with a short capelet, double-breasted jacket with gold buttons and a navy bow tie, a pleated mini skirt, white ruffled gloves, WHITE THIGH-HIGH SOCKS with small icy-blue side ribbons, and black mary jane shoes), standing on a round white display base, exactly as shown in <Image 1>: same sculpt, same paint, same pose, same base.
<Image 1> is the reference photo of the figure.

summary:
[text-to-video] A product turntable shot: the figure of <Subject 1> on its base rotates smoothly a full 360 degrees clockwise and returns exactly to the starting angle, on a plain light grey studio backdrop with soft even lighting. Seamless loop.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - the figure's sculpt, outfit details, colours, glossy PVC-like finish and the white round base from <Image 1>. Nothing is added or removed.
<Image 1>: reference - the plain light grey backdrop and soft studio lighting ARE kept.

detailed_description:
Photorealistic product video of a collectible figure. [Shot 1] Fixed camera at the figure's eye level, slightly below, centered, no camera movement, no zoom. The turntable rotates at constant speed: the figure starts facing the camera, turns to show its right side, its back, its left side, and ends facing the camera again at exactly the starting angle, so the last frame matches the first frame. Soft shadows on the base move with the rotation. The figure itself does not move or change pose. Whole figure and base always fully visible with margin above the head.

overall_soundscape:
Silence.

non_diegetic_music:
None.
```

> ライセンス: 生成モデルは MiniMax H3（MiniMax H3 Community License）。利用時は「MiniMax H3」の表示と AI 生成の開示を。
