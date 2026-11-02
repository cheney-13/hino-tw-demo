(() => {
  /* hero carousel */
  const slides = $$('#hero .hero-slide'), bar = $('#heroBar');
  let i = 0, paused = false, t;
  $('[data-hero-n]').textContent = slides.length;
  const go = n => {
    i = (n + slides.length) % slides.length;
    slides.forEach((s, k) => s.classList.toggle('on', k === i));
    $('[data-hero-i]').textContent = String(i + 1).padStart(2, '0');
    restart();
  };
  const restart = () => { clearInterval(t); if (!paused) t = setInterval(() => go(i + 1), 6000); };
  $$('[data-hero]').forEach(b => b.addEventListener('click', () => go(i + +b.dataset.hero)));
  const pb = $('[data-hero-pause]');
  pb.addEventListener('click', () => {
    paused = !paused; bar.classList.toggle('paused', paused);
    pb.querySelector('use').setAttribute('href', paused ? '#i-play' : '#i-pause');
    pb.setAttribute('aria-label', paused ? '播放輪播' : '暫停輪播');
    restart();
  });
  restart();

  /* hot models: 500 series sub-menu */
  $$('[data-hot]').forEach(c => {
    c.addEventListener('click', e => { if (e.target.closest('[data-hot-x]')) { e.stopPropagation(); c.classList.remove('open'); return; } if (!e.target.closest('a')) c.classList.add('open'); });
    c.addEventListener('keydown', e => { if (e.key === 'Enter') c.classList.add('open'); });
  });
  document.addEventListener('click', e => $$('[data-hot].open').forEach(c => { if (!c.contains(e.target)) c.classList.remove('open'); }));
})();
