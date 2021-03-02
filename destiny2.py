import hoshino
import os,base64
import requests as req
from PIL import Image
from io import BytesIO
from hoshino import Service, R
from .get_zhoubao_info import *
from .get_xur_info import *
from .get_chall_info import *
from .get_zhu_info import *


sv_help = '''
[周报] 查看命运2周报
[老九] 查看老九位置和装备
[试炼] 查看试炼周报
[蛛王] 查看蛛王商店
[光尘] 查看光尘商店
[百科] 小黑盒百科链接
'''.strip()

#帮助界面
sv = Service('destiny2', help_=sv_help, bundle='命运2订阅')

os.mkdir(R.img('destiny2').path)

#周报功能
@sv.on_fullmatch(('周报','命运2周报'))
async def zhoubao(bot, ev):
    bot = hoshino.get_bot()
    response = req.get(getzhoubaoImg(sethtml1()))
    ls_f = base64.b64encode(BytesIO(response.content).read())
    imgdata = base64.b64decode(ls_f)
    save_dir = R.img('destiny2').path
    path_dir = os.path.join(save_dir,'zhoubao.jpg')
    file = open(path_dir,'wb')
    # 以base64的形式写入文件，用于下载图片
    file.write(imgdata)
    file.close()
    # 先用下面这个形式写，万一以后要加新功能呢
    pzhoubao = ' '.join(map(str, [
        R.img(f'destiny2/zhoubao.jpg').cqcode,
    ]))
    msg = f'命运2 周报：\n图片作者：seanalpha\n{pzhoubao}'
    await bot.send(ev, msg)

#老九功能
@sv.on_fullmatch(('老九','仄','九','xur','老仄','苏尔'))
async def xur(bot, ev):
    response = req.get(getxurImg(sethtml2()))
    ls_f = base64.b64encode(BytesIO(response.content).read())
    imgdata = base64.b64decode(ls_f)
    save_dir = R.img('destiny2').path
    path_dir = os.path.join(save_dir,'xur.jpg')
    file = open(path_dir,'wb')
    file.write(imgdata)
    file.close()
    pxur = ' '.join(map(str, [
        R.img(f'destiny2/xur.jpg').cqcode,
    ]))
    msg = f'命运2 仄：\n图片作者：seanalpha\n{pxur}'
    await bot.send(ev, msg)

#试炼周报功能
@sv.on_fullmatch(('试炼','奥斯里斯试炼','试炼周报'))
async def chall(bot, ev):
    response = req.get(getchallImg(sethtml3()))
    ls_f = base64.b64encode(BytesIO(response.content).read())
    imgdata = base64.b64decode(ls_f)
    save_dir = R.img('destiny2').path
    path_dir = os.path.join(save_dir,'shilian.jpg')
    file = open(path_dir,'wb')
    file.write(imgdata)
    file.close()
    pshilian = ' '.join(map(str, [
        R.img(f'destiny2/shilian.jpg').cqcode,
    ]))
    msg = f'命运2 试炼周报：\n图片作者：seanalpha\n{pshilian}'
    await bot.send(ev, msg)

#蛛王商店功能
@sv.on_fullmatch(('蛛王','蛛王商店','猪王'))
async def zhu(bot, ev):
    response = req.get(getzhuImg(sethtml4()))
    ls_f = base64.b64encode(BytesIO(response.content).read())
    imgdata = base64.b64decode(ls_f)
    save_dir = R.img('destiny2').path
    path_dir = os.path.join(save_dir,'zhuwang.jpg')
    file = open(path_dir,'wb')
    file.write(imgdata)
    file.close()
    pzhuwang = ' '.join(map(str, [
        R.img(f'destiny2/zhuwang.jpg').cqcode,
    ]))
    msg = f'命运2 蛛王：\n图片来源：小黑盒百科\n注意小黑盒蛛王信息可能更新较慢\n{pzhuwang}'
    await bot.send(ev, msg)

#光尘商店（为了图方便，这里直接放了一张整个赛季的商店图片）
@sv.on_fullmatch(('光尘','光尘商店'))
async def buy(bot, ev):
    response = req.get("https://cdn.jsdelivr.net/gh/azmiao/picture-bed/img/buy-13.jpg")
    ls_f = base64.b64encode(BytesIO(response.content).read())
    imgdata = base64.b64decode(ls_f)
    save_dir = R.img('destiny2').path
    path_dir = os.path.join(save_dir,'guangchen.jpg')
    file = open(path_dir,'wb')
    file.write(imgdata)
    file.close()
    pguangchen = ' '.join(map(str, [
        R.img(f'destiny2/guangchen.jpg').cqcode,
    ]))
    msg = f'命运2 第13赛季光尘商店：\n{pguangchen}'
    await bot.send(ev, msg)

#百科后续打算做成其他形式，但目前直接放了个链接，自己去小黑盒看吧
@sv.on_fullmatch(('百科','命运2百科'))
async def baike(bot, ev):
    msg = '命运2 百科链接\n https://api.xiaoheihe.cn/wiki/get_homepage_info_for_app/?wiki_id=1085660&is_share=1 \n来自: 小黑盒'
    await bot.send(ev, msg)
