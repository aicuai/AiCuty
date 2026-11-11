'use strict';
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#nav');
function closeMenu() { navigation.classList.remove('is-open'); menuButton.setAttribute('aria-expanded', 'false'); }
menuButton.addEventListener('click', () => { const open = navigation.classList.toggle('is-open'); menuButton.setAttribute('aria-expanded', String(open)); });
navigation.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
document.addEventListener('keydown', event => { if (event.key === 'Escape' && navigation.classList.contains('is-open')) { closeMenu(); menuButton.focus(); } });
const slides = [
  { image: 'hero', alt: 'ステージに集まるAiCutyの6人', kicker: 'MEET AiCuty', title: '6人と、つぎの物語へ。', href: '#members' },
  { image: 'music', alt: '紫のネオンが輝く渋谷に立つサキ・ノワール', kicker: 'SAKI NOIRE / MUSIC', title: 'Shibuya in the Dark', href: 'https://youtu.be/GaYYt1cDleY' },
  { image: 'marsha-story', alt: '書店で本を抱えるマーシャ・アランチャ', kicker: 'MARSHA ARANCIA', title: '本とカルチャーの、その先へ。', href: '#marsha-profile' }
];
let slide = 0;
function showSlide(change) {
  slide = (slide + change + slides.length) % slides.length;
  const item = slides[slide]; const image = document.querySelector('#hero-image');
  image.src = `assets/site/${item.image}.webp`; image.alt = item.alt;
  document.querySelector('#hero-kicker').textContent = item.kicker;
  document.querySelector('#hero-title').textContent = item.title;
  document.querySelector('#hero-link').href = item.href;
  document.querySelector('#slide-count').textContent = `${String(slide + 1).padStart(2, '0')} / 03`;
}
document.querySelector('#previous').addEventListener('click', () => showSlide(-1));
document.querySelector('#next').addEventListener('click', () => showSlide(1));
const search = document.querySelector('#member-search');
const members = [...document.querySelectorAll('.member')];
const normalize = text => text.normalize('NFKC').toLocaleLowerCase().replace(/[\s・]/g, '');
search.addEventListener('input', () => {
  const term = normalize(search.value); let visible = 0;
  members.forEach(member => { member.hidden = !normalize(member.dataset.search).includes(term); if (!member.hidden) visible++; else member.querySelector('audio').pause(); });
  document.querySelector('#no-results').hidden = visible !== 0;
});
const players = [...document.querySelectorAll('audio')];
players.forEach(player => player.addEventListener('play', () => players.forEach(other => { if (other !== player) other.pause(); })));
document.querySelectorAll('[data-voice]').forEach(select => select.addEventListener('change', () => {
  const player = select.closest('.profile').querySelector('audio'); player.pause();
  player.src = `voice/${select.dataset.voice}/${select.dataset.voice}-v3-${select.value}.mp3`; player.load();
}));
document.querySelectorAll('details').forEach(details => details.addEventListener('toggle', () => { if (!details.open) details.querySelector('audio').pause(); }));
function openProfile() {
  const target = document.getElementById(location.hash.slice(1));
  if (target?.matches('details')) {
    search.value = ''; members.forEach(member => { member.hidden = false; });
    document.querySelector('#no-results').hidden = true; target.open = true;
    requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
  }
}
window.addEventListener('hashchange', openProfile); openProfile();

document.addEventListener('click', event => {
  const link = event.target.closest('a[href^="#"]');
  if (link && link.hash === location.hash && link.hash.endsWith('-profile')) { event.preventDefault(); openProfile(); }
});
