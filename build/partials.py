import time
VER = time.strftime("%Y%m%d%H%M")
CAR = "300.html"
LOGO = '<span class="logo"><img src="assets/img/hino-logo.svg" alt="HINO" width="195" height="32"><img class="tag" src="assets/img/logo-tagline.png" alt="HINO TRUST 驅動未來" width="219" height="32"></span>'

def alinks(v):
    return "".join('<a href="#">%s</a>' % x for x in v)

def lilinks(v):
    return "".join('<li><a href="#">%s</a></li>' % x for x in v)

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
<symbol id="i-close" viewBox="0 0 24 24"><path d="M5 5l14 14M19 5L5 19"/></symbol>
<symbol id="i-pause" viewBox="0 0 24 24"><path d="M9 5v14M15 5v14"/></symbol>
<symbol id="i-play" viewBox="0 0 24 24"><path d="M7 4l12 8-12 8z"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><path d="M4 12.5l5 5L20 6.5"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M3 7h18M3 12h18M3 17h18"/></symbol>
<symbol id="i-mail" viewBox="0 0 24 24"><path d="M3 5h18v14H3z"/><path d="M3 6l9 7 9-7"/></symbol>
<symbol id="i-fb" viewBox="0 0 24 24"><path d="M14 21v-8h3l.5-3.5H14V7.6c0-1 .3-1.6 1.7-1.6H18V3a23 23 0 0 0-2.7-.1C12.6 2.9 11 4.5 11 7.3v2.2H8V13h3v8"/></symbol>
<symbol id="i-line" viewBox="0 0 24 24"><path d="M3 4h18v13H10l-4 3v-3H3z"/><path d="M7 8v5h2M11 8v5M14 13V8l3 5V8"/></symbol>
<symbol id="i-truck" viewBox="0 0 24 24"><path d="M5 3h14v15H5z"/><path d="M5 8h14M3 9v4M21 9v4M7 18v3M17 18v3M8 14h1M15 14h1"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2z"/></symbol>
<symbol id="i-cal" viewBox="0 0 24 24"><path d="M3 5h18v16H3zM3 10h18M8 3v4M16 3v4"/></symbol>
<symbol id="i-calc" viewBox="0 0 24 24"><path d="M5 2h14v20H5z"/><path d="M8 5h8v4H8zM8 13h.01M12 13h.01M16 13h.01M8 17h.01M12 17h.01M16 17h.01"/></symbol>
<symbol id="i-trophy" viewBox="0 0 24 24"><path d="M7 3h10v6a5 5 0 0 1-10 0z"/><path d="M7 5H3v2a4 4 0 0 0 4 4M17 5h4v2a4 4 0 0 1-4 4M12 14v4M7 21h10M9 18h6"/></symbol>
<symbol id="i-sprout" viewBox="0 0 24 24"><path d="M12 22V10M12 13c0-5 3-8 9-8 0 5-3 8-9 8zM12 15c0-4-3-7-8-7 0 4 3 7 8 7zM3 22l4-6M21 22l-4-6"/></symbol>
<symbol id="i-bus" viewBox="0 0 24 24"><path d="M4 3h16v15H4z"/><path d="M4 9h16M2 7v4M22 7v4M7 18v3M17 18v3M7 14h2M15 14h2M9 6h6"/></symbol>
<symbol id="i-grid" viewBox="0 0 24 24"><path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z"/></symbol>
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
NAV = ["車款介紹", "據點查詢", "售後服務", "車主專區", "最新消息", "品牌介紹"]
MENU = {
    "據點查詢": ("menu-loc.jpg", "LOCATIONS", ["北部地區", "中部地區", "南部地區", "東部地區"]),
    "售後服務": ("menu-svc.jpg", "SERVICE", ["保養維修", "保固服務", "微笑大使", "獎學金計畫", "優良駕駛", "FAQ"]),
    "車主專區": ("menu-own.jpg", "OWNERS", ["車主登入", "車輛操作影片", "車主小幫手", "HINO 好集利", "和泰購", "FAQ"]),
    "最新消息": ("menu-news.jpg", "NEWS", ["品牌新聞", "活動資訊", "中獎公告"]),
    "品牌介紹": ("menu-brand.jpg", "ABOUT", ["品牌故事", "T 商旅車", "iTRAQ"]),
}

def sub_link(t, href="#"):
    return f'<a class="mm-link" href="{href}"><span>{t}</span>{ic("right","s16")}</a>'

def header():
    groups = "".join(
        f'<div class="mm-grp{" on" if n.startswith("300") else ""}" data-big="{big}" data-img="{img}"><span class="b">{b}</span><a class="n" href="{CAR}">{n}</a>{"".join(sub_link(x, CAR) for x in subs)}</div>'
        for b, n, d, img, big, subs in CARS)
    car_mega = f'<div class="mega"><div class="mega-in"><div class="mega-l car"><span class="big" data-mm-big>300系</span><img src="assets/img/car-300.webp" alt="" data-mm-img></div><div class="mega-r"><h3>車款介紹</h3><div class="mm-cars">{groups}</div></div></div></div>'
    items = ""
    for i, n in enumerate(NAV):
        if i == 0:
            items += f'<li class="has-mega"><a class="nav-a" href="{CAR}">{n}</a>{car_mega}</li>'
        else:
            img, en, links = MENU[n]
            items += f'<li class="has-mega"><a class="nav-a" href="#">{n}</a><div class="mega"><div class="mega-in"><div class="mega-l"><img src="assets/img/{img}" alt="" loading="lazy"><span class="en">{en}</span></div><div class="mega-r"><h3>{n}</h3><div class="mm-grid">{"".join(sub_link(x) for x in links)}</div></div></div></div></li>'
    mcars = "".join(
        f'<div class="mcar"><a class="mcar-h" href="{CAR}"><img src="assets/img/{img}" alt=""><div><span class="b">{b}</span><b>{n}</b></div></a>{"".join(sub_link(x, CAR) for x in subs)}</div>'
        for b, n, d, img, big, subs in CARS)
    macc = f'<details><summary>車款介紹{ic("plus","pm")}</summary><div class="mnav-sub">{mcars}</div></details>' + "".join(
        f'<details><summary>{k}{ic("plus","pm")}</summary><div class="mnav-sub plain">{"".join(sub_link(x) for x in v[2])}</div></details>'
        for k, v in MENU.items())
    return f"""<header class="hdr" id="top">
<div class="wrap hdr-in">
<a class="hdr-logo" href="index.html" aria-label="HINO 首頁">{LOGO}</a>
<nav class="hdr-nav" aria-label="主選單"><ul>{items}</ul>
<div class="hdr-icons"><a href="#" aria-label="聯絡我們">{ic("mail")}</a><a href="#" aria-label="Facebook">{ic("fb")}</a><a href="#" aria-label="LINE">{ic("line")}</a></div></nav>
<button class="hdr-burger" data-open-menu aria-label="開啟選單">{ic("menu","s28")}</button>
</div></header>
<div class="mnav" id="mnav" aria-hidden="true">
<div class="mnav-top"><a href="index.html">{LOGO}</a><button class="mnav-x" data-close-menu aria-label="關閉選單">{ic("up","s28")}</button></div>
<div class="mnav-body">{macc}
<button class="btn btn-red btn-block mnav-cta" data-modal="m-drive" style="justify-content:center">預約試乘</button>
<div class="mnav-links"><a href="#" data-modal="m-contact">聯絡我們</a><a href="#">Facebook</a><a href="#">LINE 加入好友</a></div>
<p class="mnav-tel">客服專線<a href="tel:0800522567">0800-522-567</a></p></div>
</div>"""

def footer():
    cars = [c[1] for c in CARS]
    car_li = ""
    for n in cars:
        if n.startswith("300"):
            car_li += f'<li><button class="ftr-car" data-ftr-car>{n}{ic("plus","s16")}</button><div class="ftr-car-sub"><a href="{CAR}">5/6.5/7.4/7.5/8噸</a><a href="{CAR}">5噸木床貨斗</a></div></li>'
        else:
            car_li += f'<li><button class="ftr-car" data-ftr-car>{n}{ic("plus","s16")}</button><div class="ftr-car-sub"><a href="{CAR}">查看{n}</a></div></li>'
    cols = {
        "據點查詢": ["北部地區", "中部地區", "南部地區", "東部地區"],
        "售後服務": ["保養維修", "保固服務", "微笑大使", "獎學金計畫", "優良駕駛", "FAQ"],
        "車主專區": ["車主登入", "車輛操作影片", "車主小幫手", "HINO 好集利", "和泰購", "FAQ"],
        "最新消息": ["品牌新聞", "活動資訊", "中獎公告"],
        "品牌介紹": ["品牌故事", "T 商旅車", "iTRAQ"],
    }
    other = "".join(f'<div><h3>{k}</h3><ul>{lilinks(v)}</ul></div>' for k, v in cols.items())
    rel1 = "".join(f'<dd><a href="#">{x}</a></dd>' for x in ["大車友善地圖", "TOYOTA商旅車", "iTRAQ"])
    rel2 = "".join(f'<dd><a href="#">{x}</a></dd>' for x in ["和泰汽車新聞室", "長源汽車", "HINO Global", "日野自動車（日本）", "和泰產險", "和運租車", "和安保險", "和泰 GO"])
    return f"""<footer>
<section class="ftr-cta"><div class="wrap">
<div><h2>CONTACT</h2><p>需要協助嗎？歡迎與我們聯繫</p></div>
<div class="btns">
<a class="btn btn-line" href="{CAR}"><span>{ic("truck","s28")}車款介紹</span>{ic("arrow")}</a>
<a class="btn btn-line" href="#"><span>{ic("pin","s28")}據點查詢</span>{ic("arrow")}</a>
<a class="btn btn-line" href="#" data-modal="m-contact"><span>{ic("mail","s28")}聯絡我們</span>{ic("arrow")}</a>
</div></div></section>
<div class="wrap ftr-map"><span class="logo"><img src="assets/img/hino-logo.svg" alt="HINO" width="195" height="32"><img class="tag" src="assets/img/logo-tagline.png" alt="HINO TRUST 驅動未來" width="219" height="32"></span>
<div class="ftr-cols"><div><h3>車款介紹</h3><ul>{car_li}</ul></div>{other}</div></div>
<div class="ftr-rel"><div class="wrap"><dl><dt>相關服務</dt>{rel1}</dl><dl><dt>相關網站</dt>{rel2}</dl></div></div>
<div class="ftr-bot"><div class="wrap"><div class="l"><span>總代理：和泰汽車股份有限公司</span><div class="links" style="display:flex;gap:20px"><a href="#">契約書下載</a><a href="#">隱私權聲明</a><a href="tel:0800522567">客服專線 0800-522-567</a></div></div><div class="r">Copyright © Hotai Motor Co., Ltd. All rights reserved.</div></div></div>
</footer>
<div class="demo-flag">DEMO・示意網頁</div>"""

def sidenav():
    return f"""<aside class="sidenav" id="sidenav" aria-label="快速服務">
<div class="sn-panel" id="snPanel">
<a class="sn-act" href="#">{ic("pin","s28")}尋找據點</a>
<button class="sn-act" data-modal="m-contact">{ic("phone","s28")}專人聯繫</button>
<button class="sn-act" data-modal="m-drive">{ic("cal","s28")}預約試乘</button>
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
<body>
{SPRITE}
{header()}
<main>
{body}
</main>
{footer()}
{sidenav()}
{modals()}
<script src="assets/js/main.js?v={VER}" defer></script>{scripts}
</body>
</html>
"""
