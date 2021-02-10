import os, hoshino
from nonebot import *
from hoshino import Service, R
from .get_zhoubao_info import *
from .get_xur_info import *
from .get_chall_info import *
from .get_zhu_info import *


#帮助界面
sv = Service("destiny2")

help_txt = '''
[周报] 查看命运2周报
[老九] 查看老九位置和装备
[试炼] 查看试炼周报
[蛛王] 查看蛛王商店
[光尘] 查看光尘商店
[百科] 小黑盒百科链接
'''
@sv.on_command('命运2帮助',only_to_me=False)
async def help(bot):
    await bot.send(help_txt)

#周报功能
@sv.on_command('周报',aliases=('命运2周报'),only_to_me=False)
async def zhoubao(session: CommandSession):
    img1 = MessageSegment.image(getzhoubaoImg(sethtml1()))
    #print(getzhoubaoImg(html))
    msg = '命运2 周报：\n图片作者：seanalpha\n'
    msg = msg + str(img1)
    await session.send(msg)

#老九功能
@sv.on_command('老九',aliases=('仄','九','xur','老仄','苏尔'),only_to_me=False)
async def xur(session: CommandSession):
    img2 = MessageSegment.image(getxurImg(sethtml2()))
    #print(getxurImg(html))
    msg = '命运2 仄：\n图片作者：seanalpha\n'
    msg = msg + str(img2)
    await session.send(msg)

#试炼周报功能
@sv.on_command('试炼',aliases=('奥斯里斯试炼'),only_to_me=False)
async def chall(session: CommandSession):
    img3 = MessageSegment.image(getchallImg(sethtml3()))
    #print(getchallImg(html))
    msg = '命运2 试炼周报：\n图片作者：seanalpha\n'
    msg = msg + str(img3)
    await session.send(msg)

#蛛王商店功能
@sv.on_command('蛛王',aliases=('蛛王商店','猪王'),only_to_me=False)
async def zhu(session: CommandSession):
    img4 = MessageSegment.image(getzhuImg(sethtml4()))
    #print(getzhuImg(html))
    msg = '命运2 蛛王：\n图片来源：小黑盒百科\n'
    msg = msg + str(img4)
    await session.send(msg)

#光尘商店（为了图方便，这里直接放了一张整个赛季的商店图片）
@sv.on_command('光尘',aliases=('光尘商店'),only_to_me=False)
async def buy(session: CommandSession):
    img5 = MessageSegment.image("https://cdn.jsdelivr.net/gh/azmiao/picture-bed/img/buy-14.jpg")
    msg = '命运2 第14赛季光尘商店：\n'
    msg = msg + str(img5)
    await session.send(msg)

#百科后续打算做成其他形式，但目前直接放了个链接，自己去小黑盒看吧
@sv.on_command('百科',aliases=('命运2百科'),only_to_me=False)
async def baike(session: CommandSession):
    msg = '命运2 百科链接\n https://api.xiaoheihe.cn/wiki/get_homepage_info_for_app/?wiki_id=1085660&is_share=1 \n来自: 小黑盒'
    await session.send(msg)
