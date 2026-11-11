"""Rebuild homepage WebP derivatives from tracked original artwork (requires Pillow)."""
from pathlib import Path
from PIL import Image
root = Path(__file__).resolve().parents[1]
target = root / 'docs/assets/site'
target.mkdir(parents=True, exist_ok=True)
assets = {**{name: f'img/anime/{name}.png' for name in ('elena', 'mei', 'mina', 'nao', 'saki', 'marsha')},
          'hero': 'img/AiCuty-6.png',
          'music': 'SakiNoire/SakiNoire-20260925-ShibuyaInTheDark.png',
          'marsha-story': 'MarshaArancia/MarshaArancia-KeyVisual.png'}
for name, source in assets.items():
    with Image.open(root / source) as image:
        image.thumbnail((1600, 1100) if name == 'hero' else (960, 1000))
        image.save(target / f'{name}.webp', quality=86, method=6)
print(f'Generated {len(assets)} optimized images; originals unchanged.')
