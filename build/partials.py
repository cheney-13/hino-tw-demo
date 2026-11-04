import time
VER = time.strftime("%Y%m%d%H%M%S")
CAR = "300.html"
LOGO = '<span class="logo"><img src="assets/img/hino-logo.svg" alt="HINO" width="195" height="32"><img class="tag" src="assets/img/logo-tagline.png" alt="HINO TRUST 驅動未來" width="219" height="32"></span>'

def alinks(v):
    return "".join('<a href="#">%s</a>' % x for x in v)

def lilinks(v, noop=False):
    return "".join('<li><a href="#"%s>%s</a></li>' % (" data-noop" if noop else "", x) for x in v)

def ic(name, cls=""):
    return f'<svg class="ico {cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M4 12h15M13 6l6 6-6 6"/></symbol>
<symbol id="i-left" viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></symbol>
<symbol id="i-right" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></symbol>
<symbol id="i-down" viewBox="0 0 24 24"><path d="M5 9l7 7 7-7"/></symbol>
<symbol id="i-up" viewBox="0 0 24 24"><path d="M5 15l7-7 7 7"/></symbol>
<symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 4v16M4 12h16"/></symbol>
<symbol id="i-minus" viewBox="0 0 24 24"><path d="M4 12h16"/></symbol>
<symbol id="i-close" viewBox="0 0 24 24"><path d="M6 6L18 18M18 6L6 18"/></symbol>
<symbol id="i-pause" viewBox="0 0 24 24"><path d="M9 5v14M15 5v14"/></symbol>
<symbol id="i-play" viewBox="0 0 24 24"><path d="M7 4l12 8-12 8z"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="M4 12.5l5 5L20 6.5"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M3 7h18M3 12h18M3 17h18"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><path d="M3 5h18v14H3z"/><path d="M3 6l9 7 9-7"/></symbol>
<symbol id="i-fb" viewBox="0 0 24 24"><path d="M14 21v-8h3l.5-3.5H14V7.6c0-1 .3-1.6 1.7-1.6H18V3a23 23 0 0 0-2.7-.1C12.6 2.9 11 4.5 11 7.3v2.2H8V13h3v8"/></symbol>
<symbol id="i-line" viewBox="0 -0.5 24 25"><path d="M1 2H23V17H13L8 22V17H1V2Z"/><path d="M18.5671 8.92728C18.8844 8.92728 19.1399 9.18637 19.1399 9.50091C19.1399 9.81455 18.8844 10.0736 18.5671 10.0736H16.9717V11.0964H18.5671C18.8844 11.0964 19.1399 11.3536 19.1399 11.6691C19.1399 11.9818 18.8844 12.2409 18.5671 12.2409H16.398C16.0844 12.2409 15.828 11.9818 15.828 11.6691V7.33182C15.828 7.01818 16.0844 6.75909 16.4008 6.75909H18.5699C18.8844 6.75909 19.1399 7.01818 19.1399 7.33182C19.1399 7.64909 18.8844 7.90455 18.5671 7.90455H16.9717V8.92728H18.5671ZM15.0626 11.6691C15.0626 11.9145 14.9044 12.1327 14.6699 12.2109C14.6117 12.23 14.549 12.2391 14.489 12.2391C14.2971 12.2391 14.1335 12.1573 14.0253 12.0118L11.8044 8.99637V11.6691C11.8044 11.9818 11.5508 12.2409 11.2308 12.2409C10.9162 12.2409 10.6617 11.9818 10.6617 11.6691V7.33182C10.6617 7.08637 10.819 6.86819 11.0526 6.79091C11.1071 6.77 11.1762 6.76091 11.229 6.76091C11.4062 6.76091 11.5699 6.85546 11.679 6.99182L13.9171 10.0191V7.33182C13.9171 7.01818 14.1735 6.75909 14.4899 6.75909C14.8035 6.75909 15.0626 7.01818 15.0626 7.33182V11.6691ZM9.8435 11.6691C9.8435 11.9818 9.58714 12.2409 9.26986 12.2409C8.95623 12.2409 8.69986 11.9818 8.69986 11.6691V7.33182C8.69986 7.01818 8.95623 6.75909 9.27259 6.75909C9.58714 6.75909 9.8435 7.01818 9.8435 7.33182V11.6691ZM7.60168 12.2409H5.43259C5.11895 12.2409 4.85986 11.9818 4.85986 11.6691V7.33182C4.85986 7.01818 5.11895 6.75909 5.43259 6.75909C5.74895 6.75909 6.00532 7.01818 6.00532 7.33182V11.0964H7.60168C7.91805 11.0964 8.1735 11.3536 8.1735 11.6691C8.1735 11.9818 7.91714 12.2409 7.60168 12.2409Z" fill="currentColor" stroke="none"/></symbol>
<symbol id="i-truck" viewBox="0 0 24 24"><path d="M5 3h14v15H5z"/><path d="M5 8h14M3 9v4M21 9v4M7 18v3M17 18v3M8 14h1M15 14h1"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 22L5 13V7L8 3H16L19 7V13L12 22Z"/><path d="M10 8H14V12H10V8Z"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M4 3H9L11 9L8 11C9.5 14 11 15.5 13 16L15 13L21 15V20H17C10 20 4 14 4 7V3Z"/></symbol>
<symbol id="i-cal" viewBox="0 0 24 24"><path d="M3 5H21V21H3V5Z"/><path d="M3 10H21M8 3V7M16 3V7"/></symbol>
<symbol id="i-ig" viewBox="0 0 24 24"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17 7h.01"/></symbol>
<symbol id="i-yt" viewBox="0 0 24 24"><rect x="2.5" y="5" width="19" height="14" rx="4"/><path d="M10 9v6l5-3z"/></symbol>
<symbol id="i-dl" viewBox="0 0 24 24"><path d="M12 3V15M7 10L12 15L17 10M4 20H20"/></symbol>
<symbol id="i-calc" viewBox="0 0 24 24"><path d="M5 2h14v20H5z"/><path d="M8 5h8v4H8zM8 13h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01M16 17h.01"/></symbol>
<symbol id="i-trophy" viewBox="0 0 24 24"><path d="M7 3h10v6a5 5 0 0 1-10 0z"/><path d="M7 5H3v2a4 4 0 0 0 4 4M17 5h4v2a4 4 0 0 1-4 4M12 14v4M7 21h10M9 18h6"/></symbol>
<symbol id="i-sprout" viewBox="0 0 24 24"><path d="M12 15V8"/><path d="M12 10C12 6.5 9.5 4.5 5.5 4.5C5.5 8 8 10 12 10Z"/><path d="M12 8C12 5 14.2 3 17.8 3C17.8 6 15.6 8 12 8Z"/><path d="M3 15H21"/><path d="M12 15V18M12 18L9 21M12 18L15 21M9.5 15.5L7 18M14.5 15.5L17 18"/></symbol>
<symbol id="i-bus" viewBox="0 0 24 24"><path d="M4 3h16v15H4z"/><path d="M4 9h16M2 7v4M22 7v4M7 18v3M17 18v3M7 14h2M15 14h2M9 6h6"/></symbol>
<symbol id="i-grid" viewBox="0 0 24 24"><path d="M10 4H4V10H10V4ZM20 4H14V10H20V4ZM10 14H4V20H10V14ZM20 14H14V20H20V14Z"/></symbol>
<symbol id="i-zoom" viewBox="0 0 24 24"><circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/></symbol>
</svg>"""

CARS = [
    # brand, name, desc, img, big label, sub items
    ("日野", "小型貨車 200系列", "3.49 噸", "car-200.webp", "200系", ["3.49噸"]),
    ("日野", "300系中小型貨車", "5/6.5/7.4/7.5/8 噸・5 噸木床貨斗", "car-300.webp", "300系", ["5/6.5/7.4/7.5/8噸", "5噸木床貨斗"]),
    ("日野", "500系中型貨車", "10.4/11・15.5/17 噸大貨車", "car-500.webp", "500系", ["10.4/11噸大貨車", "15.5/17噸大貨車", "17噸鋁合金鷗翼大貨車"]),
    ("日野", "700系大型貨車", "6x2・4x2・6x4", "car-700.webp", "700系", ["6x2 大貨車", "4x2 曳引車", "6x4 大貨車/砂石車/混凝土攪拌車"]),
    ("日野", "大型巴士", "RK・RM 360P", "car-bus-l.webp", "BUS", ["RK大客車", "RM 360P大客車"]),
    ("豐田", "中型巴士", "COASTER", "car-bus-m.webp", "COASTER", ["COASTER"]),
    ("日野", "油電複合動力系列", "6.5/8 噸", "car-hybrid.webp", "HYBRID", ["6.5/8噸"]),
]
NAV = ["車款介紹", "售後服務", "車主專區", "最新消息", "品牌與活動"]
MENU = {
    "售後服務": ("menu-svc.jpg", "SERVICE", ["保養維修", "正廠零配件", "原廠嚴選輪胎", "道路救援服務", "保固條件", "FAQ"]),
    "車主專區": ("menu-own.jpg", "OWNERS", ["車主登入", "HINO 好集利", "HINO 精品", "HOTAI 購", "HINO 車主小幫手", "車輛操作影片", "FAQ"]),
    "最新消息": ("menu-news.jpg", "NEWS", ["購車優惠", "品牌新聞", "活動資訊", "中獎公告"]),
    "品牌與活動": ("menu-brand.jpg", "BRAND", ["HINO TRUST", "微笑大使", "獎學金計畫", "優良駕駛", "大車友善地圖", "車隊管理 iTRAQ", "TOYOTA 商旅車"]),
}

def sub_link(t, href="#"):
    return f'<a class="mm-link" href="{href}"><span>{t}</span>{ic("right","s16")}</a>'

def header():
    groups = "".join(
        f'<div class="mm-grp{" on" if n.startswith("300") else ""}" data-img="menu-{img}"><span class="b">{b}</span><a class="n" href="{CAR}">{n}</a>{"".join(sub_link(x, CAR) for x in subs)}</div>'
        for b, n, d, img, big, subs in CARS)
    car_mega = f'<div class="mega"><div class="mega-in"><div class="mega-l car"><img src="assets/img/menu-car-300.webp" alt="" data-mm-img></div><div class="mega-r"><h3>車款介紹</h3><div class="mm-cars">{groups}</div></div></div></div>'
    items = ""
    for i, n in enumerate(NAV):
        if i == 0:
            items += f'<li class="has-mega"><a class="nav-a" href="{CAR}">{n}</a>{car_mega}</li>'
        else:
            img, en, links = MENU[n]
            items += f'<li class="has-mega"><a class="nav-a" href="#">{n}</a><div class="mega"><div class="mega-in sm"><div class="mega-l"><img src="assets/img/{img}?v={VER}" alt="" loading="lazy"><span class="en">{en}</span></div><div class="mega-r"><h3>{n}</h3><div class="mm-grid">{"".join(sub_link(x) for x in links)}</div></div></div></div></li>'
    mcars = "".join(
        f'<div class="mcar"><a class="mcar-h" href="{CAR}"><img src="assets/img/{img}?v={VER}" alt=""><div><span class="b">{b}</span><b>{n}</b></div></a>{"".join(sub_link(x, CAR) for x in subs)}</div>'
        for b, n, d, img, big, subs in CARS)
    macc = f'<details><summary>車款介紹{ic("plus","pm")}</summary><div class="mnav-sub">{mcars}</div></details>' + "".join(
        f'<details><summary>{k}{ic("plus","pm")}</summary><div class="mnav-sub plain">{"".join(sub_link(x) for x in v[2])}</div></details>'
        for k, v in MENU.items())
    return f"""<header class="hdr" id="top">
<div class="wrap hdr-in">
<a class="hdr-logo" href="index.html" aria-label="HINO 首頁">{LOGO}</a>
<nav class="hdr-nav" aria-label="主選單"><ul>{items}</ul>
<div class="hdr-icons"><a href="#" aria-label="聯絡我們">{ic("mail")}</a><a href="#" aria-label="LINE">{ic("line")}</a><a href="#" aria-label="Facebook">{ic("fb")}</a><a href="#" aria-label="Instagram">{ic("ig")}</a><a href="#" aria-label="YouTube">{ic("yt")}</a></div></nav>
<button class="hdr-burger" data-open-menu aria-label="開啟選單"><img src="assets/img/icon-menu.svg" alt="" width="60" height="60"></button>
</div></header>
<div class="page-dim" aria-hidden="true"></div>
<div class="mnav" id="mnav" aria-hidden="true">
<div class="mnav-top"><a href="index.html">{LOGO}</a><button class="mnav-x" data-close-menu aria-label="關閉選單"><img src="assets/img/icon-menu-close.svg" alt="" width="60" height="60"></button></div>
<div class="mnav-body">{macc}
<div class="mnav-links"><a href="#" data-modal="m-contact">聯絡我們</a><a href="#">LINE</a><a href="#">Facebook</a><a href="#">Instagram</a><a href="#">YouTube</a></div>
<p class="mnav-tel">客服專線<a href="tel:0800522567">0800-522-567</a></p></div>
</div>"""

def footer(car=False):
    car_li = "".join(
        f'<li class="ser"><button type="button" class="ser-h" data-ftr-car aria-expanded="false"><span>{n}</span>{ic("plus","s16")}</button><div class="ser-links">{"".join(f"<a href={chr(34)}#{chr(34)} data-noop>{x}</a>" for x in subs)}</div></li>'
        for b, n, d, img, big, subs in CARS)
    cols = {k: v[2] for k, v in MENU.items()}
    other = "".join(f'<div class="col"><h3>{k}</h3><ul>{lilinks(v, True)}</ul></div>' for k, v in cols.items())
    rel = lambda xs: "".join(f'<a href="#" data-noop>{x}</a>' for x in xs)
    rel1 = rel(["大車友善地圖", "TOYOTA商旅車", "iTRAQ"])
    rel2 = rel(["和泰汽車新聞室", "長源汽車", "HINO Global", "日野自動車（日本）", "和泰產險", "和運租車", "和安保險", "和泰 GO"])
    cbtn = lambda href, icon, label, extra="": f'<a class="cbtn" href="#" data-noop>{ic(icon,"s28")}<span>{label}</span>{ic("arrow","s20 arr")}</a>'
    dl_b = f'<a href="#" data-noop>{ic("dl")}<span>下載型錄</span></a>' if car else ""
    return f"""<footer class="ftr">
<section class="ftr-cta"><div class="fw">
<div class="t"><h2>CONTACT</h2><p>需要協助嗎？歡迎與我們聯繫</p></div>
<div class="btns">{cbtn("#","pin","尋找據點")}{cbtn("#","phone","專人聯繫")}{cbtn("#","mail","聯絡我們")}</div>
</div></section>
<div class="ftr-map"><div class="fw">{LOGO}
<div class="ftr-cols"><div class="col"><h3>車款介紹</h3><ul>{car_li}</ul></div>{other}</div></div></div>
<div class="ftr-rel"><div class="fw"><dl><dt>相關服務</dt><dd>{rel1}</dd></dl><dl><dt>相關網站</dt><dd>{rel2}</dd></dl></div></div>
<div class="ftr-bot"><div class="fw"><div class="l"><span class="corp">總代理：和泰汽車股份有限公司</span><span class="links"><a href="#" data-noop>契約書下載</a><a href="#" data-noop>隱私權聲明</a><a href="#" data-noop>客服專線 0800-522-567</a></span></div><div class="r">Copyright © Hotai Motor Co., Ltd. All rights reserved.</div></div></div>
</footer>
<nav class="bnav" aria-label="快速服務">
<a href="#">{ic("pin")}<span>尋找據點</span></a>
<button type="button" data-modal="m-contact">{ic("phone")}<span>專人聯繫</span></button>
<button type="button" data-modal="m-drive">{ic("cal")}<span>預約試乘</span></button>{dl_b}
</nav>
<div class="demo-flag">DEMO・示意網頁</div>"""

def sidenav(car=False):
    dl = f'<a class="sn-act" href="#" data-noop>{ic("dl","s28")}下載型錄</a>' if car else ""
    return f"""<aside class="sidenav" id="sidenav" aria-label="快速服務">
<div class="sn-panel" id="snPanel">
<a class="sn-act" href="#">{ic("pin","s28")}尋找據點</a>
<button class="sn-act" data-modal="m-contact">{ic("phone","s28")}專人聯繫</button>
<button class="sn-act" data-modal="m-drive">{ic("cal","s28")}預約試乘</button>{dl}
<button class="sn-close" data-sidenav aria-controls="snPanel">{ic("close","s28")}收合</button>
</div>
<div class="sn-fab-wrap"><button class="sn-fab" data-sidenav aria-controls="snPanel" aria-expanded="false">{ic("grid","s28")}快速服務</button></div>
</aside>"""

def modal(mid, title, body, foot="", cls=""):
    ft = f'<div class="modal-ft">{foot}</div>' if foot else ""
    return f"""<div class="modal" id="{mid}" role="dialog" aria-modal="true" aria-labelledby="{mid}-t" aria-hidden="true">
<div class="modal-scrim" data-close></div>
<div class="modal-box {cls}"><div class="modal-hd"><h3 id="{mid}-t">{title}</h3><button class="modal-x" data-close aria-label="關閉">{ic("close")}</button></div>
{body}{ft}</div></div>"""

def chips(items, on=None, name=""):
    return '<div class="chips" data-chips="%s">%s</div>' % (name, "".join(
        f'<button type="button" class="chip{" on" if x == on else ""}">{x}</button>' for x in items))

def verify_block(prefix):
    return f"""<div class="fld"><label>手機號碼<span class="req">必填</span></label>
<div class="inp-wrap"><input class="inp" type="tel" inputmode="tel" placeholder="0912-345-678" data-phone>
<button type="button" class="btn-sm" data-send disabled>取得驗證碼</button><span class="ok" hidden>{ic("check","s20")}已驗證</span></div>
<p class="hint" data-phone-hint>我們會發送簡訊驗證碼，確認號碼正確</p></div>
<div class="fld" data-code-fld><label>簡訊驗證碼<span class="req">必填</span></label>
<input class="inp" inputmode="numeric" maxlength="6" placeholder="請輸入 6 位數驗證碼" data-code disabled>
<p class="hint" data-code-hint>請先取得驗證碼</p></div>"""

AGREE = lambda t: f'<label class="agree"><input type="checkbox" class="sr" data-agree><span class="cbx">{ic("check")}</span>{t}</label>'

CITIES = ["台北市", "新北市", "桃園市", "台中市", "台南市", "高雄市"]

def modals():
    city_opts = "".join(f"<option>{c}</option>" for c in CITIES)
    contact = f"""<div class="modal-bd" data-flow="contact">
<div data-step="form">
<p class="fm-intro">留下聯絡方式，將由您選擇的據點專人與您聯繫，說明報價、分期與購車優惠。</p>
<div class="fld"><span class="lb">有興趣的車款</span><div class="sel-row"><span>300 系</span><b>6.5 噸 標準座艙手排</b></div></div>
<div class="fld"><label>姓名<span class="req">必填</span></label><input class="inp" placeholder="王大明" data-name></div>
{verify_block("c")}
<div class="fld"><label>希望聯繫的據點<span class="req">必填</span></label><div class="grid2">
<select class="inp" data-city><option value="">請選擇縣市</option>{city_opts}</select>
<select class="inp" data-branch disabled><option value="">請選擇據點</option></select></div></div>
<div class="fld"><span class="lb">方便聯絡的時段</span>{chips(["平日上午","平日下午","平日晚上","假日"],"平日下午","time")}</div>
<div class="fld"><span class="lb">預計購車時間</span>{chips(["1 個月內","3 個月內","半年內","還在評估"],None,"when")}</div>
{AGREE("我已閱讀並同意《個人資料蒐集告知事項》，同意和泰汽車及所屬經銷商與我聯繫。")}
</div>
<div data-step="done" hidden><div class="done"><div class="badge">{ic("check")}</div><h4>已收到您的資料</h4><p data-done-lead>專人將與您聯繫，請留意來電。</p>
<dl class="sum"><div><dt>車款</dt><dd>300 系 6.5 噸 標準座艙手排</dd></div><div><dt>聯絡電話</dt><dd data-s-phone></dd></div><div><dt>聯繫據點</dt><dd data-s-branch></dd></div><div><dt>方便時段</dt><dd data-s-time></dd></div></dl>
<p class="hint">若需更改資料，可直接撥打客服專線 0800-522-567。</p></div></div>
</div>"""
    contact_ft = f'<button class="btn btn-red btn-block" data-submit disabled>送出資料{ic("arrow")}</button><button class="btn btn-dark btn-block" data-close data-finish hidden>完成{ic("arrow")}</button>'

    area_opts = "".join(f"<option>{c}</option>" for c in ["北部地區", "中部地區", "南部地區", "東部地區"])
    drive = f"""<div class="modal-bd" data-flow="drive">
<div data-step="form">
<p class="fm-intro">預約試乘車輛需進行調度，實際試乘日期及時段，將由專人與您聯繫確認後排定。</p>
<div class="step-no"><em>01</em>試乘車款</div>
<div class="fld"><label>試乘車款<span class="req">必填</span></label><div class="grid2"><select class="inp"><option>小型貨車</option></select><select class="inp" data-car><option>300 系列 5 噸</option><option>300 系列 6.5 噸</option></select></div></div>
<div class="step-no"><em>02</em>聯絡資料</div>
<div class="fld"><label>姓名<span class="req">必填</span></label><input class="inp" placeholder="王大明" data-name></div>
<div class="fld"><span class="lb">性別<span class="req">必填</span></span>{chips(["先生","小姐"],"先生","gender")}</div>
<div class="fld"><label>公司行號名稱（選填）</label><input class="inp" placeholder="請輸入公司行號名稱"></div>
{verify_block("d")}
<div class="fld"><span class="lb">客服人員聯絡時間</span>{chips(["08:00~10:00","12:00~16:00","16:00 以後","皆可"],"皆可","ctime")}</div>
<div class="step-no"><em>03</em>試乘時間與地點</div>
<div class="fld"><label>期望日期<span class="req">必填</span></label><input class="inp" type="date" data-date><p class="hint">實際日期以專人聯繫確認為準</p></div>
<div class="fld"><span class="lb">期望時段<span class="req">必填</span></span>{chips(["08:00~10:00","10:00~12:00","12:00~14:00","14:00~16:00"],"10:00~12:00","slot")}</div>
<div class="fld"><span class="lb">試乘方式<span class="req">必填</span></span>{chips(["營業所試乘","到府試乘"],"營業所試乘","way")}</div>
<div class="fld"><label>試乘據點<span class="req">必填</span></label><div class="grid2"><select class="inp" data-city><option value="">請選擇區域</option>{area_opts}</select><select class="inp" data-branch disabled><option value="">請選擇營業所</option></select></div></div>
{AGREE("我已閱讀並同意《試乘條款》及《個人資料蒐集告知事項》。")}
</div>
<div data-step="done" hidden><div class="done"><div class="badge">{ic("check")}</div><h4>已收到您的試乘預約</h4><p>試乘車輛需進行調度，專人將與您聯繫，確認實際試乘日期與時段。</p>
<dl class="sum"><div><dt>試乘車款</dt><dd data-s-car></dd></div><div><dt>期望時間</dt><dd data-s-when></dd></div><div><dt>試乘地點</dt><dd data-s-branch></dd></div><div><dt>聯絡電話</dt><dd data-s-phone></dd></div></dl>
<p class="hint">若需更改資料，可直接撥打客服專線 0800-522-567。</p></div></div>
</div>"""
    drive_ft = f'<button class="btn btn-red btn-block" data-submit disabled>確定送出{ic("arrow")}</button><button class="btn btn-dark btn-block" data-close data-finish hidden>完成{ic("arrow")}</button>'

    calc = f"""<div class="modal-bd"><div class="calc" id="calc">
<div>
<span class="lb">車款</span><div class="sel-row"><span>車型</span><b>6.5 噸 標準艙手排</b></div>
<div class="kv"><span>建議售價</span><b>NT$ 1,580,000</b></div>
<span class="lb">頭期款</span><div class="dp"><b data-c-pct>30%</b><span data-c-dp>NT$ 474,000</span></div>
<input type="range" min="10" max="50" step="5" value="30" data-c-range aria-label="頭期款比例"><div class="rg-lb"><span>10%</span><span>50%</span></div>
<span class="lb">分期期數</span><div class="terms chips" data-chips="term">{"".join(f'<button type="button" class="chip{" on" if t==48 else ""}" data-t="{t}">{t} 期</button>' for t in (24,36,48,60))}</div>
<span class="lb">購車優惠</span><button type="button" class="bonus on" data-c-bonus><span class="cbx">{ic("check")}</span><div><b>套用購車金</b><small>指定車款最高 30 萬</small></div><em>−NT$ 300,000</em></button>
</div>
<div><div class="res"><p class="m">每月約</p><p class="big"><small>NT$</small><span data-c-month>17,840</span></p>
<dl><div><dt>建議售價</dt><dd>NT$ 1,580,000</dd></div><div><dt data-c-dpl>頭期款（30%）</dt><dd data-c-dp2>NT$ 474,000</dd></div><div><dt>購車金折抵</dt><dd data-c-b>−NT$ 300,000</dd></div><div><dt>貸款金額</dt><dd data-c-loan>NT$ 806,000</dd></div><div><dt>分期期數</dt><dd data-c-term>48 期</dd></div></dl></div>
<p class="res-note">試算結果僅供參考，實際金額依和泰車貸核定及據點報價為準。</p></div>
</div></div>"""
    calc_ft = f'<button class="btn btn-dark btn-block" data-modal="m-contact">專人聯繫{ic("arrow")}</button><button class="btn btn-red btn-block" data-modal="m-drive">預約試乘{ic("arrow")}</button>'
    return (modal("m-contact", "專人聯繫", contact, contact_ft)
            + modal("m-drive", "預約試乘", drive, drive_ft)
            + modal("m-calc", "購車試算", calc, calc_ft, "w960"))

def page(title, desc, css, body, js):
    car = bool(js) and js[0] == "car.js"
    links = "".join(f'<link rel="stylesheet" href="assets/css/{c}?v={VER}">' for c in css)
    scripts = "".join(f'<script src="assets/js/{j}?v={VER}" defer></script>' for j in js)
    return f"""<!doctype html>
<html lang="zh-Hant-TW">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' fill='%23E60012'/%3E%3Cpath d='M9 8v16M23 8v16M9 16h14' stroke='white' stroke-width='3'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700;900&family=Roboto:wght@400;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css?v={VER}">{links}
</head>
<body class="pg-{js[0].split('.')[0] if js else 'x'}">
{SPRITE}
{header()}
<main>
{body}
</main>
{footer(car)}
{sidenav(car)}
{modals()}
<script src="assets/js/main.js?v={VER}" defer></script>{scripts}
</body>
</html>
"""
