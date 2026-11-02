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

  /* PCS modal tabs */
  const pt = $$('#pcsTabs button'), pi = $$('#pcsStage img');
  pt.forEach((b, k) => b.addEventListener('click', () => { pt.forEach((x, j) => x.classList.toggle('on', j === k)); pi.forEach((x, j) => x.classList.toggle('on', j === k)); }));

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
  let onlyDiff = false; // demo: show every spec row by default
  const fields = G.map(([g, items]) => [g, items.map(([k, u, key]) => [k + (u ? `（${u}）` : ''), key])]);
  function renderCmp() {
    const ms = picked.map(id => M.find(m => m.id === id)); const n = ms.length;
    $('#cmpPill').textContent = `${st.ton} · ${st.cab} · 變速箱${st.trans}`;
    const opts = cur => match().map(m => `<option${m.id === cur ? ' selected' : ''}>${m.id}</option>`).join('');
    const cols = ms.map((m, k) => `<div class="cmp-col"><select class="inp" disabled><option>車系 300 系</option></select><div class="img"><img src="assets/img/car-300.webp" alt=""></div><select class="inp" data-k="${k}">${opts(m.id)}</select><span class="wb">軸距 ${m.wb}</span><a class="btn btn-red" href="#">型錄下載<svg class="ico s20"><use href="#i-arrow"/></svg></a></div>`).join('');
    const grps = fields.map(([g, fs]) => `<div class="cmp-grp"><h4><span>${g}</span><svg class="ico s20"><use href="#i-minus"/></svg></h4>${fs.map(([k, key]) => {
      const vals = ms.map(m => m[key]); const same = vals.every(v => v === vals[0]);
      return `<div class="cmp-row ${same ? 'same' : 'diff'}"><span class="k">${k}</span>${vals.map(v => `<span class="v">${v}</span>`).join('')}</div>`;
    }).join('')}</div>`).join('');
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
  $$('#ton button').forEach(b => b.addEventListener('click', () => {
    $$('#ton button').forEach(x => x.classList.toggle('on', x === b));
    const has = b.dataset.ton === '6.5 噸';
    $('#specBody').hidden = !has; $('#specNote').hidden = has;
  }));
  $$('table.st').forEach(tb => $$('tr.grp', tb).forEach(r => r.addEventListener('click', () => {
    const c = r.classList.toggle('closed');
    $$(`tr[data-in="${r.dataset.grp}"]`, tb).forEach(x => x.classList.toggle('hide', c));
  })));
  const sel = $('#specSel'), dl = $('#specDl');
  const KEYS = [['車輛總重', m => m.gw + ' kg'], ['全長 × 全寬', m => `${m.l} × ${m.wd} mm`], ['軸距', m => m.wb + ' mm'], ['引擎型式', m => m.eng], ['最大淨馬力', m => m.hp.replace(' / ', ' ps / ') + ' rpm'], ['最大淨扭力', m => m.tq.replace(' / ', ' kg・m / ') + ' rpm']];
  const fill = () => { const m = M[+sel.value]; dl.innerHTML = KEYS.map(([k, f]) => `<div><dt>${k}</dt><dd>${f(m)}</dd></div>`).join(''); };
  sel.addEventListener('change', fill); fill();
})();
