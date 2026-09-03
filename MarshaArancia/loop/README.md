# Marsha Arancia — ちびループダンス（MiniMax H3）

## seed 20260903

| | |
|---|---|
| ファイル | `loop-20260903.mp4`（緑背景・608×800・124 フレーム・24fps）／ `loop-20260903.webm`（クロマキー抜き・alpha） |
| モデル | MiniMax-H3 Ref2VA（pruned_int8_convrot）20 step、ComfyUI 標準ノード |
| 参照 | `marsha-chibi-green.png`（comfy-aicu `infra/bench/video/refs/`） |
| seed | 20260903 |
| 生成 | NVIDIA RTX 4000 Ada 20GB × 1、6 分、comfy-aicu Actions run 33713046415 |
| 検査 | 上余白 110px（全フレーム最小）／ 最初と最後のフレームの差 2.3（255 中） |

### プロンプト（H3-Context-IR）

```
subject_definitions:
<Subject 1> is a chibi (super-deformed, 2.5 heads tall) version of Marsha Arancia: a chibi girl with a matcha-green short bob with orange streaks and a small ahoge, bright green eyes, tan skin, orange headphones around her neck, a pop-art patterned green-yellow-orange hoodie covered in stickers, a black skirt with green polka dots over black shorts, orange dotted socks, chunky colourful sneakers and a small black backpack.
<Image 1> is the character reference for <Subject 1>, standing centered in an idle pose on a flat green background.

summary:
[text-to-video] A seamless dance loop of <Subject 1>: she starts in the exact idle pose of <Image 1>, bounces in place, jumps and spins once in midair, lands softly, strikes a cute pose, swings her arms wide left and right, and settles back into the exact starting pose so the clip repeats naturally. Fixed camera, flat chroma-key green background, no sound.

retention_analysis:
<Subject 1> (appears in [Shot 1]): fully_preserved - identity, chibi proportions, hairstyle, outfit and colours from <Image 1>. Her face, hairstyle, proportions and clothing design never change.
<Image 1>: reference - the SOLID flat green background IS carried into the target and stays exactly the same flat green for every frame. The centered full-body framing is kept.

detailed_description:
Clean 2D anime style, cel-shaded, crisp outlines. Solid flat chroma-key green background with no gradient, no floor, no shadow.
[Shot 1] Fixed wide shot from the center, camera never moves. FULL BODY ALWAYS VISIBLE WITH LARGE MARGIN: the figure is SMALL in the frame, filling only about 60% of the frame height when standing, centered, with empty green space above the head equal to at least one head height. The jumps are small hops (never higher than half a head), so even at the top of a hop the whole head and hair stay far below the top edge. The feet stay well above the bottom edge. The background is a SOLID FLAT CHROMA-KEY GREEN (#00FF00) in every single frame, exactly like <Image 1>: no dark background, no gradient, no floor, no shadow. <Subject 1> begins in the idle pose of <Image 1>, then bounces rhythmically in place, launches into a small energetic jump, spins around once in midair, lands softly, strikes a cute pose with one hand near her cheek, then swings both arms wide to the left and to the right. Hair, clothes and accessories bounce with each movement. Abrupt cuts and extreme splits are avoided; every movement flows smoothly into the next. In the final frames she settles back into the exact idle pose of <Image 1>, centered, feet together, so the loop repeats naturally.

overall_soundscape:
Silence. No music, no voice, no sound effects.

non_diegetic_music:
None.
```

> ライセンス: 生成モデルは MiniMax H3（MiniMax H3 Community License）。利用時は「MiniMax H3」の表示と AI 生成の開示を。
> キャラクターは AiCuty ガイドライン（https://www.aicu.jp/terms/aicuty-guideline）に従う。

