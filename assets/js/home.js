(() => {
  /* hero carousel — ticker text follows the active banner */
  const slides = $$('#hero .hero-slide'), bar = $('#heroBar'), track = $('#tickTrack');
  let i = 0, paused = false, t;
  $('[data-hero-n]').textContent = slides.length;
  const setTick = txt => {
    track.innerHTML = Array(4).fill(`<span>${txt}</span>`).join('');
    track.style.animation = 'none'; void track.offsetWidth; track.style.animation = '';
  };
  const go = n => {
    i = (n + slides.length) % slides.length;
    slides.forEach((s, k) => s.classList.toggle('on', k === i));
    $('[data-hero-i]').textContent = String(i + 1).padStart(2, '0');
    setTick(slides[i].dataset.tick);
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

  /* brand: parallax background logo */
  const brand = $('#brand'), plx = $('[data-parallax]');
  const reduce = matchMedia('(prefers-reduced-motion:reduce)').matches;
  const onScroll = () => {
    const r = brand.getBoundingClientRect();
    if (r.bottom < 0 || r.top > innerHeight) return;
    const p = (r.top + r.height / 2 - innerHeight / 2) / innerHeight; // -1..1
    plx.style.transform = `translate3d(0,${(p * 90).toFixed(1)}px,0)`;
  };
  if (!reduce) { addEventListener('scroll', onScroll, { passive: true }); onScroll(); }

  /* brand: count up red numbers when visible */
  const nums = $$('[data-count]');
  const run = el => {
    const end = +el.dataset.count, dur = 1400, t0 = performance.now();
    const step = now => {
      const k = Math.min(1, (now - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      el.textContent = Math.round(end * e);
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  if (!reduce) {
    nums.forEach(n => n.textContent = '0');
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } }), { threshold: .6 });
    nums.forEach(n => io.observe(n));
  }

  /* hot models: every card opens its own model-option overlay */
  const cards = $$('[data-hot]');
  cards.forEach(c => {
    c.addEventListener('click', e => {
      if (e.target.closest('[data-hot-x]')) { e.stopPropagation(); c.classList.remove('open'); return; }
      if (e.target.closest('a')) return;
      cards.forEach(x => x !== c && x.classList.remove('open'));
      c.classList.add('open');
    });
    c.addEventListener('keydown', e => { if (e.key === 'Enter' && e.target === c) c.click(); if (e.key === 'Escape') c.classList.remove('open'); });
  });
  document.addEventListener('click', e => cards.forEach(c => { if (!c.contains(e.target)) c.classList.remove('open'); }));
})();
