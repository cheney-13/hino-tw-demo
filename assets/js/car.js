(() => {
  const M = window.MODELS, G = window.GROUPS;
  const mobile = () => matchMedia('(max-width:767px)').matches;

  /* tabs scroll-spy */
  const tabs = $$('#tabs a'), secs = tabs.map(a => document.getElementById(a.dataset.spy));
  const spy = () => {
    const y = scrollY + 200; let cur = null;
    secs.forEach((s, k) => { if (s.getBoundingClientRect().top + scrollY <= y) cur = k; });
    tabs.forEach((a, k) => a.classList.toggle('on', k === cur));
    const on = tabs[cur]; if (on && mobile()) on.parentNode.scrollTo({ left: on.offsetLeft - 40, behavior: 'smooth' });
  };
  addEventListener('scroll', spy, { passive: true }); spy();

  /* interior carousel */
  $$('[data-carousel]').forEach(c => {
    const track = $('.car-track', c), dots = $$('.car-dots button', c), n = dots.length; let i = 0;
    const go = k => { i = (k + n) % n; track.style.transform = `translateX(${-100 * i}%)`; dots.forEach((d, j) => d.classList.toggle('on', j === i)); $('[data-c-i]', c).textContent = i + 1; };
    $$('[data-c]', c).forEach(b => b.addEventListener('click', () => go(i + +b.dataset.c)));
    dots.forEach((d, j) => d.addEventListener('click', () => go(j)));
    let x0; c.addEventListener('touchstart', e => x0 = e.touches[0].clientX, { passive: true });
    c.addEventListener('touchend', e => { const dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) go(i + (dx < 0 ? 1 : -1)); });
  });

  /* ---------- selector ---------- */
  const st = { ton: '6.5 噸', cab: '寬座艙', trans: '不限' };
  let picked = ['XZU710L-WFTQVR3', 'XZU720L-WFTQVR3', 'XZU710L-WFFQWR3'];
  const max = () => mobile() ? 2 : 3;
  const rows = $$('#selRows .sel-row');
  rows.forEach(r => {
    r.addEventListener('click', e => {
      const o = e.target.closest('[data-o]');
      if (o) { st[r.dataset.f] = o.dataset.o; r.classList.remove('open'); render(); e.stopPropagation(); return; }
      const was = r.classList.contains('open'); rows.forEach(x => x.classList.remove('open')); if (!was) r.classList.add('open');
    });
    r.addEventListener('keydown', e => { if (e.key === 'Enter' && e.target === r) r.click(); });
  });
  document.addEventListener('click', e => { if (!e.target.closest('#selRows')) rows.forEach(x => x.classList.remove('open')); });
  const match = () => st.ton !== '6.5 噸' ? [] : M.filter(m => (st.cab === '不限' || m.cab === st.cab) && (st.trans === '不限' || m.trans === st.trans));
  function render() {
    rows.forEach(r => { const v = st[r.dataset.f]; $('[data-v]', r).textContent = v; $$('.dd button', r).forEach(b => b.classList.toggle('on', b.dataset.o === v)); });
    const list = match(), ids = list.map(m => m.id);
    picked = picked.filter(p => ids.includes(p));
    if (!picked.length) picked = ids.slice(0, Math.min(2, max()));
    picked = picked.slice(0, max());
    const box = $('#models');
    if (!list.length) {
      $('#selRes').textContent = '符合 0 款車型';
      box.innerHTML = `<div class="empty">${st.ton} 車型資料待客戶提供（DEMO 目前僅建置 6.5 噸）</div>`;
    } else {
      $('#selRes').textContent = `符合 ${list.length} 款車型，最多可勾選 ${max()} 款比較`;
      box.innerHTML = list.map(m => {
        const on = picked.includes(m.id), dis = !on && picked.length >= max();
        return `<button class="model${on ? ' on' : ''}${dis ? ' dis' : ''}" data-id="${m.id}" aria-pressed="${on}"><span class="cbx${on ? ' on' : ''}"><svg class="ico"><use href="#i-check"/></svg></span><b>${m.id}</b><span>軸距 ${m.wb}<br>（${m.trans}）</span></button>`;
      }).join('');
    }
    const btn = $('#cmpBtn');
    btn.disabled = picked.length < 2;
    btn.firstChild.textContent = picked.length >= 2 ? `比較這 ${picked.length} 款` : '請勾選 2 款以上比較';
  }
  $('#models').addEventListener('click', e => {
    const b = e.target.closest('.model'); if (!b || b.classList.contains('dis')) return;
    const id = b.dataset.id;
    picked = picked.includes(id) ? picked.filter(x => x !== id) : [...picked, id];
    render();
  });
  addEventListener('resize', () => { clearTimeout(render.t); render.t = setTimeout(render, 200); });
  render();

  /* ---------- compare modal ---------- */
  const cmp = $('#m-cmp');
  let onlyDiff = true; // default: show only the rows that differ
  const fields = G.map(([g, items]) => [g, items.map(([k, u, key]) => [k + (u ? `（${u}）` : ''), key])]);
  function renderCmp() {
    const ms = picked.map(id => M.find(m => m.id === id)); const n = ms.length;
    $('#cmpPill').textContent = `${st.ton} · ${st.cab} · 變速箱${st.trans}`;
    const opts = cur => match().map(m => `<option${m.id === cur ? ' selected' : ''}>${m.id}</option>`).join('');
    const chev = '<svg class="ico s16"><use href="#i-down"/></svg>';
    const cols = ms.map((m, k) => `<div class="cmp-col"><div class="cmp-dd"><small>車系</small><b>300 系</b>${chev}</div><div class="img"><img src="assets/img/car-300.webp?v=2" alt=""></div><label class="cmp-dd"><b>${m.id}</b>${chev}<select data-k="${k}" aria-label="切換型號">${opts(m.id)}</select></label><span class="wb">軸距 ${m.wb}</span><a class="btn btn-red" href="#" data-noop>型錄下載<i><svg class="ico s16"><use href="#i-arrow"/></svg></i></a></div>`).join('');
    const sameGrp = fs => fs.every(([, key]) => ms.every(m => m[key] === ms[0][key]));
    const grps = fields.map(([g, fs]) => { const fold = mobile() && sameGrp(fs);
      return `<div class="cmp-grp${fold ? ' closed' : ''}"><h4><span>${g}</span>${fold ? `<em>${n} 款規格相同</em>` : ''}<svg class="ico s20"><use href="#i-${fold ? 'plus' : 'minus'}"/></svg></h4>${fs.map(([k, key]) => {
      const vals = ms.map(m => m[key]); const same = vals.every(v => v === vals[0]);
      return `<div class="cmp-row ${same ? 'same' : 'diff'}"><span class="k">${k}</span>${vals.map(v => `<span class="v">${v}</span>`).join('')}</div>`;
    }).join('')}</div>`; }).join('');
    const body = $('#cmpBody');
    body.style.setProperty('--n', n);
    body.classList.toggle('only-diff', onlyDiff);
    body.innerHTML = `<div class="cmp-cols"><p class="cmp-note">桌機最多比較 3 款，可點選型號下拉切換</p>${cols}</div>${grps}`;
    $$('select[data-k]', body).forEach(s => s.addEventListener('change', () => {
      const k = +s.dataset.k; const other = picked.indexOf(s.value);
      if (other > -1) picked[other] = picked[k];
      picked[k] = s.value; render(); renderCmp();
    }));
    $$('.cmp-grp h4', body).forEach(h => h.addEventListener('click', () => {
      const c = h.parentNode.classList.toggle('closed'); $('use', h).setAttribute('href', c ? '#i-plus' : '#i-minus');
    }));
  }
  cmp.addEventListener('modal:open', renderCmp);
  $$('#cmpSeg button').forEach(b => b.addEventListener('click', () => {
    onlyDiff = b.dataset.diff === '1';
    $$('#cmpSeg button').forEach(x => x.classList.toggle('on', x === b));
    $('#cmpBody').classList.toggle('only-diff', onlyDiff);
  }));

  /* ---------- spec ---------- */
  const SP = window.SPEC, val = (t, g, k, i) => { const r = SP[t].sections.find(x => x[0] === g)[1].find(x => x[0] === k); return r ? r[1][i] : ''; };
  const sel = $('#specSel'), dl = $('#specDl');
  let ton = '6.5 噸';
  const KEYS = [['車輛總重', i => val(ton, '重量', '車輛總重（kg）', i) + ' kg'], ['全長 × 全寬', i => `${val(ton, '底盤尺寸', '全長（mm）', i)} × ${val(ton, '底盤尺寸', '全寬（mm）', i)} mm`], ['軸距', i => val(ton, '底盤尺寸', '軸距（mm）', i) + ' mm'], ['引擎型式', i => val(ton, '引擎', '型號', i)], ['最大淨馬力', i => val(ton, '引擎', '最大淨馬力（ps/rpm）', i).replace(' / ', ' ps / ') + ' rpm'], ['最大淨扭力', i => val(ton, '引擎', '最大淨扭力（kg•m/rpm）', i).replace(' / ', ' kg・m / ') + ' rpm']];
  const fill = () => { const i = +sel.value; dl.innerHTML = KEYS.map(([k, f]) => { let v = f(i); if (v.startsWith('—')) v = '—'; return `<div><dt>${k}</dt><dd>${v}</dd></div>`; }).join(''); };
  const setTon = t => {
    ton = t;
    $$('#ton button').forEach(x => x.classList.toggle('on', x.dataset.ton === t));
    $$('#specBody table.st').forEach(tb => { tb.hidden = tb.dataset.ton !== t; });
    sel.innerHTML = SP[t].models.map((m, i) => `<option value="${i}">${m.name} ${m.id}</option>`).join('');
    fill();
    window.dispatchEvent(new CustomEvent('spec-ton', { detail: t }));
  };
  $$('#ton button').forEach(b => b.addEventListener('click', () => setTon(b.dataset.ton)));
  $$('table.st').forEach(tb => $$('tr.grp', tb).forEach(r => r.addEventListener('click', () => {
    const c = r.classList.toggle('closed');
    $$(`tr[data-in="${r.dataset.grp}"]`, tb).forEach(x => x.classList.toggle('hide', c));
  })));
  sel.addEventListener('change', fill); setTon(ton);
})();

/* full spec drawer (mobile): one model at a time, sections collapsible */
(() => {
  const SP = window.SPEC, box = document.getElementById('fullM'), sel = document.getElementById('fullSel'), tsel = document.getElementById('fullTonSel');
  if (!SP || !box) return;
  let ton = '6.5 噸';
  const draw = () => {
    const i = +sel.value, S = SP[ton].sections;
    document.getElementById('fullModel').textContent = sel.options[sel.selectedIndex].text;
    box.innerHTML = S.map(([g, rows], k) => `<section class="fs${k === 0 ? ' open' : ''}"><h4><span>${g}</span><em>${rows.length} 項</em><svg class="ico s20"><use href="#i-${k === 0 ? 'minus' : 'plus'}"/></svg></h4><dl class="rows">${rows.map(([key, vals]) => `<div class="r"><dt>${key}</dt><dd>${vals[i]}</dd></div>`).join('')}</dl></section>`).join('');
    box.querySelectorAll('.fs h4').forEach(h => h.addEventListener('click', () => {
      const on = h.parentNode.classList.toggle('open'); h.querySelector('use').setAttribute('href', on ? '#i-minus' : '#i-plus');
    }));
  };
  const setTon = t => {
    ton = t; tsel.value = t; document.getElementById('fullTon').textContent = t;
    document.querySelectorAll('.full-d table.st').forEach(tb => { tb.hidden = tb.dataset.ton !== t; });
    sel.innerHTML = SP[t].models.map((m, i) => `<option value="${i}">${m.id}</option>`).join('');
    draw();
  };
  tsel.addEventListener('change', () => setTon(tsel.value));
  window.addEventListener('spec-ton', e => setTon(e.detail));
  sel.addEventListener('change', draw); setTon(ton);
})();

/* tiles in the same row: equalise title-bar height so titles line up at the top (no fixed 2-line height) */
(() => {
  const heads = [...document.querySelectorAll('.tile .tile-h')];
  const sync = () => {
    heads.forEach(h => h.style.minHeight = '');
    const rows = new Map();
    heads.forEach(h => { const t = h.closest('.tile'); if (!t.offsetParent) return; const k = Math.round(t.getBoundingClientRect().top + scrollY); (rows.get(k) || rows.set(k, []).get(k)).push(h); });
    rows.forEach(list => { if (list.length < 2) return; const m = Math.max(...list.map(h => h.offsetHeight)); list.forEach(h => h.style.minHeight = m + 'px'); });
  };
  let t; addEventListener('resize', () => { clearTimeout(t); t = setTimeout(sync, 150); });
  if (document.fonts) document.fonts.ready.then(sync); sync();
})();

/* highlight numbers: count up when they scroll into view */
(() => {
  const ns = [...document.querySelectorAll('.nums [data-n]')];
  if (!ns.length || matchMedia('(prefers-reduced-motion:reduce)').matches) return;
  const run = el => {
    const end = +el.dataset.n, t0 = performance.now(), dur = 1400;
    const step = now => { const k = Math.min(1, (now - t0) / dur); el.textContent = Math.round(end * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step);
  };
  ns.forEach(n => n.textContent = '0');
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { $$('[data-n]', e.target).forEach(run); io.unobserve(e.target); } }), { threshold: .6 });
  document.querySelectorAll('.nums .num').forEach(n => io.observe(n));
})();

/* faq category tabs */
(() => {
  const tabs = [...document.querySelectorAll('[data-faq]')];
  tabs.forEach(b => b.addEventListener('click', () => {
    tabs.forEach(x => { const on = x === b; x.classList.toggle('on', on); x.setAttribute('aria-selected', on); });
    document.querySelectorAll('[data-faq-p]').forEach(p => { p.hidden = p.dataset.faqP !== b.dataset.faq; });
  }));
})();
