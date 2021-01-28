import datetime
import http.client
import time
import sys
from hoshino.service import Service
from hoshino import Service, R
from nonebot import *
from .get_zhoubao_info import *
from .get_xur_info import *
from .get_chall_info import *
from .get_zhu_info import *



def get_time():
    time_conn = http.client.HTTPConnection('www.baidu.com')
    time_conn.request("GET", "/")
    r = time_conn.getresponse()
    ts = r.getheader('date')
    ltime = time.strptime(ts[5:25], "%d %b %Y %H:%M:%S")
    ttime = time.localtime(time.mktime(ltime)+8*60*60)
    dat = datetime.date(ttime.tm_year,ttime.tm_mon,ttime.tm_mday)
    # 下方用于测试用
    # global testtime
    # test1 = "%u-%02u-%02u"%(ttime.tm_year,ttime.tm_mon,ttime.tm_mday)
    # test2 = "%02u:%02u:%02u"%(ttime.tm_hour,ttime.tm_min,ttime.tm_sec)
    # currenttime=test1+" "+test2
    # testtime = str(currenttime)
    return dat

def get_week_day(date):
    week_day = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期日',
    }
    day = date.weekday()
    return week_day[day]

svzb = Service('zhoubao-reminder', enable_on_default=False, help_='周报更新提醒')
svlj = Service('laojiu-reminder', enable_on_default=False, help_='老九更新提醒')
svsl = Service('shilian-reminder', enable_on_default=False, help_='试炼更新提醒')
svzw = Service('zhuwang-reminder', enable_on_default=False, help_='蛛王更新提醒')

@svzb.scheduled_job('cron', hour='03', minute='00')
async def zhoubaoreminder():
    sys.stdout.flush()
    if get_week_day(get_time()) == '星期三':
        msg0 = '今天是'
        msg1 = get_time()
        msg2 = get_week_day(get_time())
        msg31 = '\n检测到周报已更新'
        msg41 = '命运2 周报：\n图片作者：seanalpha\n'
        img1 = MessageSegment.image(getzhoubaoImg(sethtml1()))
        msg51 = msg0 + str(msg1) + str(msg2) + msg31
        msg61 = msg41 + str(img1)
        await svzb.broadcast(msg51, 'zhoubao-reminder', 0.2)
        await svzb.broadcast(msg61, 'zhoubao-reminder', 0.2)

@svlj.scheduled_job('cron', hour='03', minute='00')
async def laojiureminder():
    sys.stdout.flush()
    if get_week_day(get_time()) == '星期六':
        msg0 = '今天是'
        msg1 = get_time()
        msg2 = get_week_day(get_time())
        msg32 = '\n检测到老九已更新'
        msg42 = '命运2 仄：\n图片作者：seanalpha\n'
        img2 = MessageSegment.image(getxurImg(sethtml2()))
        msg52 = msg0 + str(msg1) + str(msg2) + msg32
        msg62 = msg42 + str(img2)
        await svlj.broadcast(msg52, 'laojiu-reminder', 0.2)
        await svlj.broadcast(msg62, 'laojiu-reminder', 0.2)

@svsl.scheduled_job('cron', hour='03', minute='00')
async def shilianreminder():
    sys.stdout.flush()
    if get_week_day(get_time()) == '星期六':
        msg0 = '今天是'
        msg1 = get_time()
        msg2 = get_week_day(get_time())
        msg33 = '\n检测到试炼周报已更新'
        msg43 = '命运2 试炼周报：\n图片作者：seanalpha\n'
        img3 = MessageSegment.image(getchallImg(sethtml3()))
        msg53 = msg0 + str(msg1) + str(msg2) + msg33
        msg63 = msg43 + str(img3)
        await svsl.broadcast(msg53, 'shilian-reminder', 0.2)
        await svsl.broadcast(msg63, 'shilian-reminder', 0.2)

@svzw.scheduled_job('cron', hour='03', minute='00')
async def zhuwangreminder():
    sys.stdout.flush()
    msg1 = get_time()
    msg0 = '今天是'
    msg2 = get_week_day(get_time())
    msg34 = '\n检测到蛛王商店已更新'
    msg44 = '命运2 蛛王：\n图片来源：小黑盒百科\n'
    img4 = MessageSegment.image(getzhuImg(sethtml4()))
    msg54 = msg0 + str(msg1) + str(msg2) + msg34
    msg64 = msg44 + str(img4)
    await svzw.broadcast(msg54, 'zhuwang-reminder', 0.2)
    await svzw.broadcast(msg64, 'zhuwang-reminder', 0.2)
