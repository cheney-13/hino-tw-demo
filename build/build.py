import os
from partials import page, ic, CAR, CARS, modal

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NEWS = [
    ("news-1.jpg", "2026/10/28", "2026年11月份 HINO外展暨試乘EVENT場次表"),
    ("news-2.jpg", "2026/10/20", "「HINO 運轉幸福家」 2026 優良駕駛頒獎典禮圓滿落幕！"),
    ("news-3.jpg", "2026/10/05", "「2026 HINO GO潮派－安全節能新體驗」11/7－11/8高雄駁二盛大登場！"),
    ("news-4.jpg", "2026/10/01", "「霸氣豪禮遇」年末購車霸氣應援！HINO享最高30萬元購車金，TOYOTA商旅車享5萬購車金！"),
]
STORIES = [
    ("story-1.jpg", "生鮮配送 · 5 噸", "清晨四點出車，貨準時到店", "「市區巷子小、停靠點多，自排開起來不累，一天跑三趟也輕鬆。」", "50% 30%"),
    ("story-2.jpg", "冷鏈業 · 6.5 噸", "冷鏈一趟不能等，穩最重要", "「滿載冷凍貨照樣有力，DPR 會自動再生，不用常停下來處理。」", "62% 50%"),
    ("story-3.jpg", "搬家業 · 8 噸", "寬座艙載人又載貨，一次到位", "「三位師傅坐得下，貨台夠長，大型家具一趟就能搬完。」", "38% 50%"),
]

def news_cards(noop=False):
    na = " data-noop" if noop else ""
    return "".join(
        f'<a class="news-card rv" href="#"{na}><div class="img"><img src="assets/img/{i}" alt="" loading="lazy"></div><div class="tx"><time>{d}</time><h3>{t}</h3></div></a>'
        for i, d, t in NEWS)

def sec_head(wm, title, eyebrow="", sub="", right=""):
    eb = f'<p class="eyebrow">{eyebrow}</p>' if eyebrow else ""
    sb = f"<small>{sub}</small>" if sub else ""
    inner = f'<div><span class="wm" aria-hidden="true">{wm}</span>{eb}<h2>{title}{sb}</h2></div>'
    if right:
        return f'<div class="sec-head row">{inner}{right}</div>'
    return f'<div class="sec-head">{inner}</div>'

# ------------------------------------------------------------------ home
def home():
    SLIDES = [
        ("運轉不凡，跨界舞動 | HINO 300 系 拚勁全開 載運新動能", "HINO 300系 拚勁全開 載運新動能"),
        ("HINO 潮好拍 創意短影音挑戰賽 | 即日起至 9/30，總獎價值 30 萬", "HINO 潮好拍 創意短影音挑戰賽"),
        ("HINO × 台灣韌性 | 品牌形象影片 現正熱映中", "HINO × 台灣韌性 品牌形象影片"),
        ("2026 HINO GO潮派－安全節能新體驗 | 11/07–11/08 高雄駁二藝術特區 B4 館", "HINO GO潮派 安全節能新體驗"),
        ("6 年/20 萬公里延長保固服務商品 | 2026 年 12 月前加購享優惠價 15,000 元", "延長保固服務商品"),
    ]
    slides = "".join(
        f'<div class="hero-slide{" on" if k == 0 else ""}" data-tick="{t}"><a href="#" data-noop><picture><source media="(max-width:767px)" srcset="assets/img/hero-m-{k+1}.jpg"><img src="assets/img/hero-{k+1}.jpg" alt="{alt}"{"" if k == 0 else " loading=lazy"}></picture></a></div>'
        for k, (t, alt) in enumerate(SLIDES))
    tick = SLIDES[0][0]
    def hot_pop(n, subs):
        return f'<div class="hot-pop"><div class="t"><b>{n}</b><button type="button" data-hot-x aria-label="關閉">{ic("close")}</button></div>{"".join(f"<a href={chr(34)}{CAR}{chr(34)}>{x}{ic(chr(97)+chr(114)+chr(114)+chr(111)+chr(119),chr(115)+chr(50)+chr(48))}</a>" for x in subs)}</div>'
    hot_small = []
    feat = None
    for b, n, s, img, big, subs in CARS:
        if n.startswith("300"):
            feat = (b, n, s, img, subs)
            continue
        hot_small.append(f'<div class="hot-card" data-hot tabindex="0" role="button" aria-label="{n}，展開車型選項"><div class="img"><img src="assets/img/{img}" alt="" loading="lazy"></div><div class="tx"><span class="b">{b}</span><b>{n}</b></div>{hot_pop(n, subs)}</div>')
    stories = "".join(
        f'<a class="story" href="#" data-noop><img src="assets/img/{i}" alt="" loading="lazy" style="object-position:{pos}"><span class="tag">{tg}</span><div class="tx"><h3>{t}</h3><p>{q}</p></div></a>'
        for i, tg, t, q, pos in STORIES * 3)
    body = f"""
<section class="wrap hero" aria-label="主視覺">
<div class="hero-stage" id="hero">{slides}</div>
<div class="hero-bar" id="heroBar">
<div class="ticker"><div class="ticker-track" id="tickTrack"><span>{tick}</span><span>{tick}</span><span>{tick}</span><span>{tick}</span></div></div>
<div class="hero-count"><div><b data-hero-i>01</b> <span>/ 0<span data-hero-n>5</span></span></div></div>
<button class="icon-btn" data-hero-pause aria-label="暫停輪播">{ic("pause")}</button>
<button class="icon-btn" data-hero="-1" aria-label="上一張">{ic("left")}</button>
<button class="icon-btn" data-hero="1" aria-label="下一張">{ic("right")}</button>
</div>
</section>

<section class="brand" id="brand">
<div class="brand-bg" aria-hidden="true"><div class="brand-track"><img src="assets/img/brand-logo.svg" alt="" data-parallax><img class="dup" src="assets/img/brand-logo.svg" alt=""></div></div>
<div class="wrap">
<div class="brand-hd rv"><p>HINO TRUST 驅動未來</p><h2>業界領導品牌<br class="m">您的最佳事業夥伴</h2></div>
<div class="stats">
<div class="stat rv">{ic("truck")}<h3>延長保固<small>里程 20 萬公里內</small></h3><p class="num">最長<b data-count="6">6</b>年</p></div>
<div class="stat rv">{ic("trophy")}<h3>銷售冠軍<small>3.49 噸以上</small></h3><p class="num"><b data-count="5">5</b>連霸</p></div>
<div class="stat rv">{ic("sprout")}<h3>在台深耕<small>和泰汽車代理</small></h3><p class="num"><b data-count="70">70</b>年以上</p></div>
</div></div>
</section>

<section class="wrap sec" aria-labelledby="hot-t">
<div class="hot">
<div class="hot-main rv" data-hot tabindex="0" role="button" aria-label="300系中小型貨車，展開車型選項"><h2 id="hot-t">熱門車款</h2><div class="img"><img src="assets/img/car-300.webp" alt="HINO 300系"></div><div class="info"><span class="b">日野</span><b>300系中小型貨車</b><span>5/6.5/7.4/7.5/8 噸・5 噸木床貨斗</span></div>{hot_pop(feat[1], feat[4])}</div>
{"".join(hot_small)}
</div>
</section>

<div class="hot-drawer" id="hotDrawer" aria-hidden="true">
<div class="hd-scrim" data-hd-close></div>
<div class="hd-sheet" role="dialog" aria-modal="true" aria-labelledby="hdName"><div class="hd-grab"></div>
<div class="hd-head"><div><span class="b" id="hdBrand"></span><b id="hdName"></b></div><button type="button" class="hd-x" data-hd-close aria-label="關閉">{ic("close","s20")}</button></div>
<div class="hd-opts" id="hdOpts"></div></div></div>

<section class="wrap sec">
{sec_head("NEWS", "最新動態", right=f'<a class="btn btn-red news-head-btn" href="#" data-noop>看更多消息{ic("arrow")}</a>')}
<div class="news">{news_cards(True)}</div>
<div class="pager"><button class="icon-btn" aria-label="上一頁">{ic("left")}</button><button class="icon-btn" aria-label="下一頁">{ic("right")}</button><div class="cnt"><div><b>01</b> <span>/ 05</span></div></div></div>
<a class="btn btn-dark btn-block news-more-m" href="#" data-noop>看更多消息{ic("arrow")}</a>
</section>

<section class="wrap sec">
{sec_head("STORIES", "車主故事", right=f'<a class="btn btn-red news-head-btn" href="#" data-noop>看更多故事{ic("arrow")}</a>')}
<div class="stories" id="stories"><div class="stories-track">{stories}<div class="stories-dup" aria-hidden="true">{stories}</div></div></div>
<a class="btn btn-dark btn-block news-more-m" href="#" data-noop>看更多故事{ic("arrow")}</a>
</section>

<section class="wrap sec">
<div class="local rv">
<div>{sec_head("LOCAL", "在地行動，和台灣一起向前行") if False else ""}<h2>在地行動，和台灣一起向前行</h2><p>秉持 HINO TRUST 精神，從優良駕駛表揚、車主照護到學子獎助，走進全台各地，與台灣一起守護每一段安全回家的路。</p></div>
<a class="act" href="#" data-noop><img src="assets/img/action-1.jpg" alt="" loading="lazy"><b>優良駕駛招募計畫</b></a>
<a class="act" href="#" data-noop><img src="assets/img/action-2.jpg" alt="" loading="lazy" style="object-position:50% 30%"><b>在學生獎學金計畫</b></a>
</div>
</section>
"""
    return page("HINO 台灣｜業界領導品牌 您的最佳事業夥伴（DEMO）", "HINO 台灣官網改版 DEMO 首頁", ["home.css"], body, ["home.js"])

# ------------------------------------------------------------------ car (300)
MODELS = [
    # id, label, cab, trans, wb, weight, len, wid, hei, eng, hp, tq, turn, gear, ton
    dict(id="XZU600L-WFMQVR3", name="標準艙手排", cab="標準座艙", trans="手排", cabf="標準座艙/低頂", gw="6,500", w="2,160", wb="2,525", l="4,670", wd="1,870", h="2,035", eng="N04C-WN", hp="150 / 2,700", tq="44.9 / 1,300~2,200", turn="5,500", gear="5 檔手排"),
    dict(id="XZU600L-WFTQVR3", name="標準艙自排", cab="標準座艙", trans="自排", cabf="標準座艙/低頂", gw="6,500", w="2,200", wb="2,525", l="4,670", wd="1,870", h="2,035", eng="N04C-WN", hp="150 / 2,700", tq="44.9 / 1,300~2,200", turn="5,500", gear="6 檔自排（附 S 檔序列式手自排）"),
    dict(id="XZU710L-WFTQVR3", name="寬座艙自排", cab="寬座艙", trans="自排", cabf="寬座艙", gw="6,500", w="2,480", wb="3,430", l="6,135", wd="1,995", h="2,215", eng="N04C-WN", hp="150 / 2,700", tq="44.9 / 1,300~2,200", turn="5,700", gear="6 檔自排（附 S 檔序列式手自排）"),
    dict(id="XZU720L-WFTQVR3", name="寬座艙自排", cab="寬座艙", trans="自排", cabf="寬座艙", gw="6,500", w="2,500", wb="3,870", l="6,750", wd="1,995", h="2,215", eng="N04C-WN", hp="150 / 2,700", tq="44.9 / 1,300~2,200", turn="6,400", gear="6 檔自排（附 S 檔序列式手自排）"),
    dict(id="XZU710L-WFFQWR3", name="寬座艙手排", cab="寬座艙", trans="手排", cabf="寬座艙", gw="6,500", w="2,455", wb="3,430", l="6,135", wd="1,995", h="2,215", eng="N04C-WP", hp="180 / 2,700", tq="47.9 / 1,400~2,600", turn="5,700", gear="6 檔手排"),
    dict(id="XZU720L-WFFQWR3", name="寬座艙手排", cab="寬座艙", trans="手排", cabf="寬座艙", gw="6,500", w="2,475", wb="3,870", l="6,750", wd="1,995", h="2,215", eng="N04C-WP", hp="180 / 2,700", tq="47.9 / 1,400~2,600", turn="6,400", gear="6 檔手排"),
]
GROUPS = [
    ("重量", [("車輛總重", "kg", "gw"), ("完成車/底盤空重", "kg", "w")]),
    ("底盤尺寸", [("軸距", "mm", "wb"), ("全長", "mm", "l"), ("全寬", "mm", "wd"), ("全高", "mm", "h")]),
    ("引擎", [("引擎型號", "", "eng"), ("最大淨馬力", "ps/rpm", "hp"), ("最大淨扭力", "kg•m/rpm", "tq")]),
    ("性能", [("最小迴轉半徑", "mm", "turn")]),
    ("底盤", [("變速箱型式", "", "gear")]),
]

def tile(img, title, desc, cls="light", extra="", open_=False, pos=""):
    st = f' style="object-position:{pos}"' if pos else ""
    btn = ic("minus" if open_ else "plus") if desc else ""
    d = f'<div class="tile-d"><div><p>{desc}</p></div></div>' if desc else ""
    oc = " open" if open_ else ""
    attr = " data-tile" if desc else ""
    return f'<div class="tile {cls}{oc} {extra}"{attr}><img src="assets/img/{img}" alt="" loading="lazy"{st}><div class="tile-b"><button class="tile-h" {"aria-expanded=" + chr(34) + ("true" if open_ else "false") + chr(34) if desc else "tabindex=-1"}>{title}{btn}</button>{d}</div></div>'

def spec_table():
    head = "".join(f'<th>{m["name"]}<small>{m["id"]}</small></th>' for m in MODELS)
    rows = f'<tr><td class="k">駕駛艙形式</td>{"".join("<td>%s</td>" % m["cabf"] for m in MODELS)}</tr>'
    for g, items in GROUPS:
        rows += f'<tr class="grp" data-grp="{g}"><td colspan="{len(MODELS)+1}">{g}{ic("up","s20")}</td></tr>'
        for k, u, key in items:
            rows += f'<tr data-in="{g}"><td class="k">{k}<u>{u}</u></td>{"".join("<td>%s</td>" % m[key] for m in MODELS)}</tr>'
    for g in ["電氣", "選擇配備", "造型/配備"]:
        rows += f'<tr class="grp closed" data-grp="{g}"><td colspan="{len(MODELS)+1}">{g}{ic("up","s20")}</td></tr><tr class="hide" data-in="{g}"><td colspan="{len(MODELS)+1}" style="color:var(--g3)">詳細配備資料待客戶提供</td></tr>'
    return f'<table class="st"><colgroup><col class="k"></colgroup><thead><tr><th>車型</th>{head}</tr></thead><tbody>{rows}</tbody></table>'

def car():
    tons = ["5 噸", "6.5 噸", "7.4 噸", "7.5 噸", "8 噸"]
    ton_btns = "".join(f'<button class="{"on" if t=="6.5 噸" else ""}" data-ton="{t}">{t}</button>' for t in tons)
    m_opts = "".join(f'<option value="{i}">{m["name"]} {m["id"]}</option>' for i, m in enumerate(MODELS))
    tabs = [("ctl", "操控"), ("eco", "節能"), ("safety", "安全"), ("power", "性能"), ("strength", "載重"), ("interior", "內裝"), ("select", "比較"), ("spec", "規配")]
    tabs_html = "".join(f'<a href="#{a}" data-spy="{a}">{t}</a>' for a, t in tabs)
    story_body = "每天清晨四點，車主就從果菜市場載滿生鮮出發，一早要跑完市區十多個停靠點，貨一定要在開店前送到。以前開手排，巷子裡走走停停，一趟下來腳都酸了。換成 300 系自排後，起步、加速都很平穩，貨物不容易晃動，長時間駕駛也輕鬆許多。"

    body = f"""
<section class="wrap">
<div class="top">
<div class="top-l">
<div class="kv"><img src="assets/img/kv-300.jpg" alt="HINO 300系 多元選擇 成就多種精彩"></div>
<div class="info"><div class="info-row"><h1>HINO 300 系 中小型貨車</h1><div class="tags"><span>5–8 噸</span><span>標準座艙/寬座艙</span><span>手排/自排</span></div></div>
<a class="promo" href="#" data-modal="m-calc">至年底，最高 30 萬購車金{ic("arrow","s20")}</a></div>
</div>
<div class="specs"><span class="wm" aria-hidden="true">SPECS</span><h2>亮點配備與數據</h2>
<button class="feat" data-modal="m-pcs"><div><b>標配 PCS＋LDWS主動安全</b><span>預警式防護＋車道偏離警示，全車型標準配備</span></div><i>{ic("arrow")}</i></button>
<div class="nums">
<div class="num"><b>5–8<small>噸</small></b><span>車輛總重</span></div>
<div class="num"><b>18<small>款</small></b><span>可選車型</span></div>
<div class="num"><b>180<small>PS</small></b><span>最大馬力</span></div>
<div class="num"><b>6<small>年</small></b><span>或 20 萬公里保固</span></div>
</div></div>
</div>
</section>
<nav class="tabs" id="tabs" aria-label="頁內導覽">{tabs_html}</nav>

<section class="wrap sec anchor" id="ctl">
{sec_head("CONTROL", "操控進化", "操控", "寬敞的中控台空間，提供多元收納功能及眾多實用性配備，讓開車更輕鬆舒適。")}
<div class="bento-ctl">
{tile("ctl-console.jpg", "寬敞中控台空間", "", "dark", "t1 rv")}
{tile("ctl-shift.jpg", "自排/手排變速箱", "除了傳統手排變速箱外，亦提供自排車型可供選擇。易於操控的自排變速箱，起步、加速更平穩，不熟練手排的駕駛者也可輕易上手，大幅降低工作負擔。", "dark", "t2 rv")}
{tile("ctl-meter.jpg", "儀錶板多功能資訊顯示幕", "大型彩色螢幕，油耗、里程、保養週期等資訊一目瞭然。", "light", "t3 rv")}
{tile("ctl-wheel.jpg", "方向盤", "配置多功能資訊顯示幕操作開關，操作更加便利。", "light", "t4 rv")}
</div></section>

<section class="wrap sec anchor" id="eco">
{sec_head("ECO", "節能環保", "節能", "DPR 柴油碳微粒主動濾清系統搭配 SCR 選擇性觸媒還原系統，降低排放汙染。")}
<div class="bento-eco">
{tile("eco-dpr.jpg", "DPR 柴油碳微粒主動濾清系統", "廢氣通過 DPF 濾清器時吸附黑煙粒狀物，堆積量過高時自動再生或提醒手動再生，降低 PM 汙染物排放。", "dark", "rv", pos="50% 20%")}
{tile("eco-scr.jpg", "選擇性觸媒還原系統（SCR）", "ECU 偵測引擎排出的廢氣，搭配 AdBlue 適時噴出尿素水，進行化學變化後，達到排氣淨化效果。", "dark", "rv")}
</div></section>

<section class="wrap sec anchor" id="safety">
<div class="safety on-dark">
{sec_head("SAFETY", "安全配備", "安全", "標配 PCS 預警式防護系統、LDWS 車道偏離警示系統、VSC 車輛穩定控制系統。")}
<div class="grid3">
{tile("safe-pcs.jpg", "PCS 預警式防護系統", "由車前方毫米波雷達及智能攝影機偵測前方行人或車輛，若系統判斷有碰撞危險時，將發出警報及支援煞車控制，降低碰撞車禍的傷害。")}
{tile("safe-ldws.jpg", "LDWS 車道偏離警示系統", "透過車輛前方所搭載的攝影機隨時偵測前方車道線，當行駛中車輛偏離車道線時，系統將會發出警示音以提醒駕駛者注意。")}
{tile("safe-view.jpg", "視野輔助系統", "搭載螢幕內嵌視野輔助系統，以 4 分割畫面同時顯示前、後、左、右鏡頭畫面並儲存紀錄。")}
</div>
<h3>煞車與車身穩定控制</h3>
<div class="grid3 sm">
{tile("safe-abs.jpg", "ABS 防鎖定煞車系統", "主動防止車輪在緊急煞車時鎖死，避免車輛失控。", pos="50% 0")}
{tile("safe-trc.jpg", "TRC 循跡防滑控制系統", "有效抑制車輛於濕滑路面起步或加速時，可能發生的輪胎打滑。", pos="50% 0")}
{tile("safe-vsc.jpg", "VSC 車輛穩定控制系統", "車輛偏離路面、轉向過度或不足時，調整動力輸出，主動掌握行車安全。", pos="50% 0")}
{tile("safe-ebd.jpg", "EBD 電子煞車力道分配系統", "因應不同行駛狀況，將前後煞車制動力做適當分配，保障駕駛者、乘客與貨物的最大安全。", pos="50% 0")}
{tile("safe-bas.jpg", "BAS 煞車輔助系統", "根據踩煞車踏板力道及速度主動判斷情況緊急與否，提供最強大的制動力。", pos="50% 0")}
{tile("safe-bos.jpg", "BOS 煞車優先系統", "油門作動時只要踩下煞車踏板，行車電腦會啟動煞車優先系統，自動降低動力輸出，使車輛減速。", pos="50% 0")}
</div></div></section>

<div class="wrap sec"><div class="pair">
<section class="sec anchor" id="power">
{sec_head("POWER", "大馬力引擎", "性能", "寬座艙手排車型搭載馬力 180PS 引擎，以大馬力支援您的行車需求。")}
<div class="feature rv" data-tile><img src="assets/img/engine.webp" alt="N04C 引擎" loading="lazy"><div class="tile-b"><button class="tile-h" aria-expanded="false">N04C 直列4缸柴油引擎{ic("plus")}</button><div class="tile-d"><div><p>電腦控制柴油直噴引擎、渦輪增壓附中間冷卻器，總排氣量 4,009 c.c.，最大淨扭力達 47.9 kg‧m。</p></div></div></div></div>
</section>
<section class="sec anchor" id="strength">
{sec_head("STRENGTH", "大樑結構", "載重", "全車採用高強度大樑，底盤耐用度高，載貨更平穩、更安全。")}
<div class="feature rv"><img src="assets/img/frame.webp" alt="高強度大樑" loading="lazy"><div class="tile-b"><div class="tile-h">高強度大樑</div></div></div>
</section>
</div></div>

<section class="wrap sec anchor" id="interior">
{sec_head("INTERIOR", "車內空間", "內裝", "貼心多元的收納功能與車內照明，實用性大幅提升。")}
<div class="bento-int">
<div class="carousel rv" data-carousel><div class="car-stage"><div class="car-track"><img src="assets/img/int-1.jpg" alt="車內照明" loading="lazy"><img src="assets/img/int-2.jpg" alt="收納空間" loading="lazy"><img src="assets/img/int-3.jpg" alt="收納空間" loading="lazy"></div>
<span class="car-cnt"><b data-c-i>1</b> / 3</span><div class="car-nav"><button data-c="-1" aria-label="上一張">{ic("left","s20")}</button><button data-c="1" aria-label="下一張">{ic("right","s20")}</button></div></div>
<div class="car-dots"><button class="on" aria-label="第 1 張"></button><button aria-label="第 2 張"></button><button aria-label="第 3 張"></button></div>
<div class="tx"><h3>多元收納與車內照明</h3><p>貼心多元的收納功能與車內照明，實用性大幅提升。＊LED 室內燈為標準座艙車型配備</p></div></div>
{tile("cab-std.webp", "標準座艙", "操控靈活，進出市區巷道不受限。", "light", "rv")}
{tile("cab-wide.webp", "寬座艙", "座艙寬廣、乘駕更舒適；貨台空間大，載貨更多元。", "light", "rv")}
</div></section>

<section class="wrap sec anchor" id="select">
<div class="select">
{sec_head("SELECT", "選出你的 300 系", "選車比較", "選噸數、座艙、變速箱，找到對應車型。")}
<div class="sel-img"><img src="assets/img/car-300.webp" alt="HINO 300系" loading="lazy"></div>
<div>
<div class="sel-rows" id="selRows">
<div class="sel-row" data-f="ton" tabindex="0"><span>噸數</span><b><em data-v>6.5 噸</em>{ic("right","s20")}</b><div class="dd">{"".join(f'<button data-o="{t}">{t}</button>' for t in tons)}</div></div>
<div class="sel-row" data-f="cab" tabindex="0"><span>座艙</span><b><em data-v>寬座艙</em>{ic("right","s20")}</b><div class="dd"><button data-o="不限">不限</button><button data-o="標準座艙">標準座艙</button><button data-o="寬座艙">寬座艙</button></div></div>
<div class="sel-row" data-f="trans" tabindex="0"><span>變速箱</span><b><em data-v>不限</em>{ic("right","s20")}</b><div class="dd"><button data-o="不限">不限</button><button data-o="手排">手排</button><button data-o="自排">自排</button></div></div>
</div>
<p class="sel-res" id="selRes"></p>
<div class="models" id="models"></div>
<button class="btn btn-red btn-block" id="cmpBtn" data-modal="m-cmp">比較這 3 款{ic("arrow")}</button>
</div></div></section>

<section class="wrap sec anchor" id="spec">
<div class="spec on-dark">
{sec_head("SPEC", "規格配備", "規格", "5 / 6.5 / 7.4 / 7.5 / 8 噸，標準座艙/寬座艙、手排/自排多種組合。")}
<div class="spec-card">
<p class="lb">噸數</p><div class="ton" id="ton">{ton_btns}</div>
<div id="specBody">
<div class="tbl-wrap">{spec_table()}</div>
<div class="spec-m"><p class="lb" style="color:var(--g3);margin-bottom:8px">型號</p><select class="inp" id="specSel">{m_opts}</select><dl id="specDl"></dl></div>
</div>
<div class="spec-note" id="specNote" hidden>此噸數規格資料待客戶提供（DEMO 目前僅建置 6.5 噸）</div>
<a class="btn btn-dark btn-block spec-m" href="#" data-modal="m-full" style="margin-top:16px;justify-content:space-between">查看完整規格表{ic("arrow")}</a>
<a class="btn btn-red btn-block" href="#">型錄下載{ic("arrow")}</a>
</div></div></section>

<section class="wrap sec anchor" id="stories">
<div class="story1 rv">
<div class="tx">{sec_head("STORIES", "車主故事")}<div class="body"><span class="tag">生鮮配送 · 5 噸</span><h3>清晨四點出車，貨準時到店</h3><p>{story_body}</p><a class="btn btn-red" href="#">看完整故事{ic("arrow")}</a></div></div>
<div class="ph"><img src="assets/img/story-3.jpg" alt="" loading="lazy"></div>
</div></section>

<section class="wrap sec">
{sec_head("NEWS", "相關資訊")}
<div class="news4">{news_cards()}</div>
</section>

<section class="wrap sec">
<div class="lead-faq">
<div class="lead rv"><div class="lead-h"><i>{ic("phone")}</i><div><b>想瞭解更多？</b><span>留下聯絡方式，由專人聯繫您</span></div></div>
<ul><li>{ic("check")}不用跑據點，專人主動與您聯繫</li><li>{ic("check")}依載運需求，推薦合適車型與配置</li><li>{ic("check")}報價、分期與購車優惠一次說明</li></ul>
<button class="btn btn-red btn-block" data-modal="m-contact">留下聯絡資料{ic("arrow")}</button>
<small>需簡訊驗證手機，約 1 分鐘完成；資料僅用於本次購車諮詢。</small></div>
<div class="faq rv">{sec_head("FAQ", "常見問答")}
<details><summary>可以分期購車嗎？{ic("plus")}</summary><p>可以。和泰提供多種車貸與分期方案，可依預算與營運需求規劃，詳情請洽各地據點業務。</p></details>
<details><summary>交車要等多久？{ic("plus")}</summary><p>依車型、配備與上裝需求不同，一般約需數週，實際交期請以據點報價為準。</p></details>
<details><summary>可以先試乘再決定嗎？{ic("plus")}</summary><p>可以。點選「預約試乘」，或直接聯繫鄰近據點安排試乘。</p></details>
<details><summary>舊車可以折抵嗎？{ic("plus")}</summary><p>可以。據點可協助舊車估價與折抵，評估結果依車況與年份而定。</p></details>
</div></div></section>
"""
    pcs = f"""<div class="modal-bd"><div class="pcs-stage" id="pcsStage"><img class="on" src="assets/img/safe-pcs.jpg" alt=""><img src="assets/img/safe-ldws.jpg" alt=""><img src="assets/img/safe-view.jpg" alt=""></div>
<div class="pcs-tabs" id="pcsTabs">
<button class="on"><b>PCS 預警式防護系統</b><span>由車前方毫米波雷達及智能攝影機偵測前方行人或車輛，若系統判斷有碰撞危險時，將發出警報及支援煞車控制，降低碰撞車禍的傷害。</span></button>
<button><b>LDWS 車道偏離警示系統</b><span>透過車輛前方所搭載的攝影機隨時偵測前方車道線，當行駛中車輛偏離車道線時，系統將會發出警示音以提醒駕駛者注意。</span></button>
<button><b>視野輔助系統</b><span>搭載螢幕內嵌視野輔助系統，以 4 分割畫面同時顯示前、後、左、右鏡頭畫面並儲存紀錄。</span></button>
</div></div>"""
    cmp_ = f"""<div class="cmp-bar"><div><span class="pill" id="cmpPill"></span><button class="edit" data-close data-goto="#select">修改選擇</button></div>
<div class="seg" id="cmpSeg"><button class="on" data-diff="1">只看差異</button><button data-diff="0">全部展開</button></div></div>
<div class="modal-bd" id="cmpBody"></div>"""
    full = f'<div class="modal-bd"><div class="tbl-wrap">{spec_table()}</div></div>'
    extra = (modal("m-pcs", "標配 PCS＋LDWS 主動安全", pcs, cls="w960")
             + modal("m-cmp", "車型比較", cmp_, cls="w1080")
             + modal("m-full", "完整規格表（6.5 噸）", full, cls="w1080"))
    import json
    data = "<script>window.MODELS=" + json.dumps(MODELS, ensure_ascii=False) + ";window.GROUPS=" + json.dumps(GROUPS, ensure_ascii=False) + ";</script>"
    html = page("HINO 300 系 中小型貨車｜HINO 台灣（DEMO）", "HINO 300 系 中小型貨車 5–8 噸，標準座艙/寬座艙、手排/自排。", ["home.css", "car.css"], body, ["car.js"])
    return html.replace("<script src=\"assets/js/main.js\"", extra + data + "<script src=\"assets/js/main.js\"", 1)

open(os.path.join(ROOT, "index.html"), "w").write(home())
open(os.path.join(ROOT, "300.html"), "w").write(car())
print("built")
