(() => {
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  window.$ = $; window.$$ = $$;

  /* header shadow */
  const hdr = $('.hdr');
  const onScroll = () => hdr.classList.toggle('scrolled', scrollY > 4);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* mega menu (hover + keyboard) */
  const syncHdr = () => hdr.classList.toggle('menu-open', !!$('.has-mega.open'));
  $$('.has-mega').forEach(li => {
    let t;
    const open = () => { clearTimeout(t); $$('.has-mega.open').forEach(x => x !== li && x.classList.remove('open')); li.classList.add('open'); syncHdr(); };
    const shut = () => { li.classList.remove('open'); syncHdr(); };
    li.addEventListener('mouseenter', open);
    li.addEventListener('mouseleave', () => { t = setTimeout(shut, 120); });
    li.addEventListener('focusin', open);
    li.addEventListener('focusout', e => { if (!li.contains(e.relatedTarget)) shut(); });
  });
  /* car mega: hovering a series swaps the left visual */
  const big = $('[data-mm-big]'), mimg = $('[data-mm-img]');
  $$('.mm-grp').forEach(g => g.addEventListener('mouseenter', () => {
    $$('.mm-grp').forEach(x => x.classList.toggle('on', x === g));
    big.textContent = g.dataset.big;
    mimg.style.opacity = 0;
    setTimeout(() => { mimg.src = 'assets/img/' + g.dataset.img; mimg.style.opacity = 1; }, 120);
  }));

  /* mobile menu */
  const mnav = $('#mnav');
  $('[data-open-menu]').addEventListener('click', () => { mnav.classList.add('open'); mnav.setAttribute('aria-hidden', 'false'); document.body.classList.add('lock'); });
  $('[data-close-menu]').addEventListener('click', closeMenu);
  function closeMenu() { mnav.classList.remove('open'); mnav.setAttribute('aria-hidden', 'true'); document.body.classList.remove('lock'); }
  $$('#mnav a').forEach(a => a.addEventListener('click', closeMenu));

  /* footer car accordion */
  $$('[data-ftr-car]').forEach(b => b.addEventListener('click', () => {
    const on = !b.classList.contains('on');
    $$('[data-ftr-car]').forEach(x => { x.classList.remove('on'); x.nextElementSibling.classList.remove('on'); x.querySelector('use').setAttribute('href', '#i-plus'); });
    if (on) { b.classList.add('on'); b.nextElementSibling.classList.add('on'); b.querySelector('use').setAttribute('href', '#i-minus'); }
  }));

  /* side nav */
  const sn = $('#sidenav');
  const setSn = closed => { sn.classList.toggle('closed', closed); $('.sn-fab', sn).setAttribute('aria-expanded', !closed); };
  if (innerWidth < 1600) setSn(true);
  $$('[data-sidenav]', sn).forEach(b => b.addEventListener('click', () => setSn(!sn.classList.contains('closed'))));

  /* modals */
  let lastFocus;
  window.openModal = id => {
    $$('.modal.open').forEach(m => close(m, true));
    const m = document.getElementById(id); if (!m) return;
    lastFocus = document.activeElement;
    m.classList.add('open'); m.setAttribute('aria-hidden', 'false'); document.body.classList.add('lock');
    m.dispatchEvent(new CustomEvent('modal:open'));
    setTimeout(() => $('.modal-x', m).focus(), 50);
  };
  function close(m, keepLock) {
    m.classList.remove('open'); m.setAttribute('aria-hidden', 'true');
    if (!keepLock) { document.body.classList.remove('lock'); lastFocus && lastFocus.focus && lastFocus.focus(); }
    m.dispatchEvent(new CustomEvent('modal:close'));
  }
  document.addEventListener('click', e => {
    const o = e.target.closest('[data-modal]');
    if (o) { e.preventDefault(); if (mnav.classList.contains('open')) closeMenu(); openModal(o.dataset.modal); return; }
    const c = e.target.closest('[data-close]');
    if (c) {
      const m = c.closest('.modal'); close(m);
      if (c.dataset.goto) document.querySelector(c.dataset.goto).scrollIntoView({ behavior: 'smooth' });
    }
  });
  addEventListener('keydown', e => { if (e.key === 'Escape') { const m = $('.modal.open'); if (m) close(m); else closeMenu(); } });

  /* chips (single select) */
  $$('[data-chips]').forEach(g => g.addEventListener('click', e => {
    const b = e.target.closest('.chip'); if (!b) return;
    $$('.chip', g).forEach(x => x.classList.toggle('on', x === b));
    g.dispatchEvent(new Event('change', { bubbles: true }));
  }));

  /* expandable tiles: whole card (incl. image) toggles; expand upward, card height fixed */
  $$('[data-tile]').forEach(t => {
    const h = $('.tile-h', t);
    t.addEventListener('click', e => {
      if (e.target.closest('a')) return;
      const on = t.classList.toggle('open');
      h.setAttribute('aria-expanded', on);
      const u = h.querySelector('use'); if (u) u.setAttribute('href', on ? '#i-minus' : '#i-plus');
    });
  });

  /* reveal on scroll */
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  $$('.rv').forEach(el => io.observe(el));

  /* ---------- form flows (contact / test drive) ---------- */
  const BRANCH = { '台北市': ['內湖據點', '士林據點'], '新北市': ['五股據點', '新店據點'], '桃園市': ['桃園據點', '中壢據點'], '台中市': ['台中據點', '大雅據點'], '台南市': ['台南據點'], '高雄市': ['高雄據點', '岡山據點'],
    '北部地區': ['五股營業所', '桃園營業所'], '中部地區': ['台中營業所'], '南部地區': ['台南營業所', '高雄營業所'], '東部地區': ['花蓮營業所'] };
  $$('[data-flow]').forEach(flow => {
    const m = flow.closest('.modal');
    const phone = $('[data-phone]', flow), send = $('[data-send]', flow), code = $('[data-code]', flow);
    const pHint = $('[data-phone-hint]', flow), cHint = $('[data-code-hint]', flow), ok = $('.ok', flow), codeFld = $('[data-code-fld]', flow);
    const city = $('[data-city]', flow), branch = $('[data-branch]', flow), agree = $('[data-agree]', flow), name = $('[data-name]', flow);
    const submit = $('[data-submit]', m), finish = $('[data-finish]', m);
    let verified = false, timer;
    const validPhone = () => /^09\d{2}-?\d{3}-?\d{3}$/.test(phone.value.trim());
    phone.addEventListener('input', () => { send.disabled = !validPhone() || verified; check(); });
    send.addEventListener('click', () => {
      code.disabled = false; code.focus();
      pHint.textContent = `驗證碼已發送至 ${phone.value}（DEMO：輸入任意 6 位數）`;
      cHint.textContent = '請輸入簡訊中的 6 位數驗證碼，10 分鐘內有效';
      let s = 60; send.disabled = true; clearInterval(timer);
      timer = setInterval(() => { s--; send.textContent = s > 0 ? `重新發送 ${s}s` : '重新發送'; if (s <= 0) { clearInterval(timer); send.disabled = false; } }, 1000);
    });
    code.addEventListener('input', () => {
      code.value = code.value.replace(/\D/g, '');
      if (code.value.length === 6) {
        verified = true; clearInterval(timer);
        send.hidden = true; ok.hidden = false; codeFld.hidden = true; phone.disabled = true;
        pHint.textContent = '此號碼已完成驗證'; pHint.classList.add('ok');
      }
      check();
    });
    city.addEventListener('change', () => {
      const list = BRANCH[city.value] || [];
      branch.innerHTML = `<option value="">${branch.options[0].text}</option>` + list.map(b => `<option>${b}</option>`).join('');
      branch.disabled = !list.length; check();
    });
    [branch, agree, name].forEach(x => x.addEventListener('input', check));
    agree.addEventListener('change', check);
    function check() { submit.disabled = !(verified && name.value.trim() && branch.value && agree.checked); }
    submit.addEventListener('click', () => {
      const chip = n => { const c = $(`[data-chips="${n}"] .chip.on`, flow); return c ? c.textContent : '—'; };
      const set = (k, v) => { const el = $(`[data-s-${k}]`, flow); if (el) el.textContent = v; };
      set('phone', phone.value); set('branch', `${city.value} ${branch.value}`); set('time', chip('time'));
      if (flow.dataset.flow === 'drive') {
        set('car', $('[data-car]', flow).value);
        const d = $('[data-date]', flow).value; set('when', `${d ? d.replace(/-/g, '/') : '待專人確認'} ${chip('slot')}`);
        set('branch', `${chip('way')}｜${city.value} ${branch.value}`);
      } else {
        $('[data-done-lead]', flow).textContent = `${city.value} ${branch.value}專人將與您聯繫，請留意來電。`;
      }
      $('[data-step="form"]', flow).hidden = true; $('[data-step="done"]', flow).hidden = false;
      submit.hidden = true; finish.hidden = false; flow.scrollTop = 0;
    });
    m.addEventListener('modal:close', () => {
      if ($('[data-step="done"]', flow).hidden) return;
      // reset after finishing
      setTimeout(() => {
        $('[data-step="form"]', flow).hidden = false; $('[data-step="done"]', flow).hidden = true;
        submit.hidden = false; finish.hidden = true; verified = false;
        phone.disabled = false; phone.value = ''; code.value = ''; code.disabled = true; codeFld.hidden = false;
        send.hidden = false; send.textContent = '取得驗證碼'; send.disabled = true; ok.hidden = true;
        pHint.textContent = '我們會發送簡訊驗證碼，確認號碼正確'; pHint.classList.remove('ok'); cHint.textContent = '請先取得驗證碼';
        name.value = ''; agree.checked = false; city.value = ''; branch.innerHTML = `<option value="">${branch.options[0].text}</option>`; branch.disabled = true; check();
      }, 300);
    });
  });

  /* ---------- calculator ---------- */
  const calc = $('#calc');
  if (calc) {
    const PRICE = 1580000, BONUS = 300000, RATE = 0.03 / 12;
    const fmt = n => n.toLocaleString('en-US');
    const range = $('[data-c-range]', calc), bonus = $('[data-c-bonus]', calc);
    const run = () => {
      const pct = +range.value, term = +$('[data-chips="term"] .chip.on', calc).dataset.t;
      const dp = Math.round(PRICE * pct / 100), b = bonus.classList.contains('on') ? BONUS : 0;
      const loan = Math.max(0, PRICE - dp - b);
      const pay = loan ? Math.round(loan * RATE / (1 - Math.pow(1 + RATE, -term))) : 0;
      $('[data-c-pct]', calc).textContent = pct + '%';
      $('[data-c-dp]', calc).textContent = $('[data-c-dp2]', calc).textContent = 'NT$ ' + fmt(dp);
      $('[data-c-dpl]', calc).textContent = `頭期款（${pct}%）`;
      $('[data-c-b]', calc).textContent = b ? '−NT$ ' + fmt(b) : 'NT$ 0';
      $('[data-c-loan]', calc).textContent = 'NT$ ' + fmt(loan);
      $('[data-c-term]', calc).textContent = term + ' 期';
      $('[data-c-month]', calc).textContent = fmt(pay);
      range.style.background = '';
    };
    range.addEventListener('input', run);
    calc.addEventListener('change', run);
    bonus.addEventListener('click', () => { bonus.classList.toggle('on'); run(); });
    run();
  }
})();
