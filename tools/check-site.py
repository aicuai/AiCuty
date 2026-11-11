"""Check the homepage's local links, anchors, assets and every voice variant."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit

root = Path(__file__).resolve().parents[1] / 'docs'
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids = []; self.urls = []; self.voices = {}; self.current_voice = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        for key in ('src', 'href'):
            if key in a: self.urls.append(a[key])
        if tag == 'select': self.current_voice = a.get('data-voice')
        if tag == 'option' and self.current_voice:
            self.voices.setdefault(self.current_voice, []).append(a['value'])
    def handle_endtag(self, tag):
        if tag == 'select': self.current_voice = None
page = Page(); page.feed((root / 'index.html').read_text())
assert len(page.ids) == len(set(page.ids)), 'Duplicate IDs'
for url in page.urls:
    u = urlsplit(url)
    if u.scheme or u.netloc: continue
    if not u.path:
        assert not u.fragment or u.fragment in page.ids, f'Missing anchor: {url}'
        continue
    path = root / u.path
    assert path.is_file() or (path.suffix == '.html' and path.with_suffix('.md').is_file()), f'Missing file: {url}'
for slug, languages in page.voices.items():
    for language in languages:
        path = root / f'voice/{slug}/{slug}-v3-{language}.mp3'
        assert path.is_file() and path.stat().st_size > 0, f'Missing voice: {path}'
assert len(page.voices) == 6
assert not (root / 'index.md').exists(), 'Duplicate Jekyll homepage'
print(f'PASS: {len(page.urls)} links/assets, {len(page.ids)} unique IDs, {sum(map(len,page.voices.values()))} voice variants, one homepage')
