# AiCuty homepage assets

`docs/index.html` is a standalone homepage for the existing Jekyll/GitHub Pages site. The previous home is preserved at `docs/about.md`. There is deliberately no `index.md` competing for `/index.html`.

- `site.css`: responsive layout, 650px/900px breakpoints and reduced-motion support.
- `site.js`: manual featured-image navigation, member search, native profile disclosures, voice-language selection. No autoplay or third-party JavaScript.
- Six member portraits: `img/anime/{elena,mei,mina,nao,saki,marsha}.png`.
- `hero.webp`: `img/AiCuty-6.png`.
- `music.webp`: `SakiNoire/SakiNoire-20260925-ShibuyaInTheDark.png`.
- `marsha-story.webp`: `MarshaArancia/MarshaArancia-KeyVisual.png`.

WebP images are size-optimized derivatives, not new character designs. Rebuild with `python tools/optimize-site-images.py` (Pillow). Original art remains untouched. Design credits are displayed in the homepage footer per repository AGENTS.md; Marsha chibi author confirmation remains pending.

## Content and maintenance

Content comes from the repository README and AGENTS.md; existing display names/colors were checked against `aicu-ai/apps/site/src/data/characters.json`. Marsha is not yet in that upstream file (existing issue #17), so her public repository sheet remains the source for this page. No private bot content is published. Reference site: https://www.nijisanji.jp/ (navigation, large visual and member discovery patterns only; no third-party brand assets or code reused).

The six `<article class="member">` entries hold public profiles and birthday/instrument information. Voice samples use existing `docs/voice/<slug>/<slug>-v3-<language>.mp3` files (19 variants). Changing the language loads a sample but does not start playback. Opening another audio player pauses the previous one. `slides` in `site.js` controls the three featured panels.

PICK UP contains evergreen links; no unverified release dates or invented news. The latest official community guideline is linked, not restated. Google Fonts is optional: system sans-serif is the fallback.

## Validation

From repository root:

```sh
python tools/check-site.py
node --check docs/assets/site/site.js
git diff --check
```

Serve `docs/` for a static homepage preview. `voices.html` and other existing Markdown pages require the normal Jekyll build; a plain file server does not render them. Existing GitHub Pages configuration is retained. No production deployment or merge is part of this branch.

Browser checks: desktop homepage, featured-image next/previous, search hit/empty/reset, profile anchors, language source switching, 390px-wide iframe mobile layout and menu navigation. This is not a physical-device test. Full Jekyll build remains to be run by GitHub Pages after merge.
