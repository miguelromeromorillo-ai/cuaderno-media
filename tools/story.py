"""Genera una historia de Instagram (1080x1920) con estética de cuaderno.
Uso: python3 story.py datos.json salida.png
datos.json: {"fecha","titulo","cifra","cifra_label","puntos":[...],"fuente"}"""
import asyncio,json,sys,html
from playwright.async_api import async_playwright
d=json.load(open(sys.argv[1]));e=html.escape
pts="".join("<li>"+e(p).replace(" %","&nbsp;%").replace(" €","&nbsp;€")+"</li>" for p in d["puntos"])
H=f"""<!doctype html><meta charset=utf-8><style>
body{{margin:0;width:1080px;height:1920px;background:#F6F0DF;font-family:Inter,sans-serif;color:#1B2540;position:relative;overflow:hidden;
background-image:repeating-linear-gradient(#F6F0DF 0 94px,#BFD0E0 94px 96px)}}
.m{{position:absolute;left:62px;top:0;bottom:0;width:4px;background:#E7A79B}}
.w{{position:absolute;left:110px;right:80px;top:300px}}
.tag{{display:inline-block;background:#1B2540;color:#F6F0DF;font-weight:800;font-size:34px;padding:12px 26px;border-radius:14px}}
h1{{font-weight:900;font-size:76px;line-height:1.08;margin:40px 0 50px}}
.c{{background:#1F8A6A;color:#fff;border-radius:28px;padding:36px 40px;box-shadow:10px 12px 0 rgba(27,37,64,.18)}}
.c b{{display:block;font-size:120px;font-weight:900;line-height:1}}.c span{{font-size:36px;font-weight:600}}
ul{{margin:50px 0 0;padding:0;list-style:none}}li{{font-size:42px;font-weight:600;line-height:1.3;margin:0 0 30px;padding-left:44px;position:relative}}
li:before{{content:'';position:absolute;left:0;top:18px;width:22px;height:22px;background:#D9432F;border-radius:50%}}
.f{{position:absolute;left:110px;right:80px;bottom:330px;font-size:28px;color:#6B7184;font-weight:600}}
.b{{position:absolute;left:110px;bottom:270px;font-family:Lora,serif;font-size:34px;opacity:.85}}
</style><div class=m></div><div class=w><span class=tag>📓 Noticia del día · {e(d['fecha'])}</span>
<h1>{e(d['titulo'])}</h1><div class=c><b>{e(d['cifra'])}</b><span>{e(d['cifra_label'])}</span></div><ul>{pts}</ul></div>
<div class=f>Fuente: {e(d['fuente'])}</div><div class=b>el cuaderno del ahorro</div>"""
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch();pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.set_content(H);await pg.evaluate("document.fonts.ready")
        await pg.screenshot(path=sys.argv[2],type="png");await b.close()
asyncio.run(main())
