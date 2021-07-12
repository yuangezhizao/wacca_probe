#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/12 21:09
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""
import datetime

import requests

from wacca_probe.models.wacca import Record

token = ''
headers = {
    'Host': 'iot.universal-space.cn',
    'Connection': 'keep-alive',
    'clienttype': 'weapp',
    'charset': 'utf-8',
    'apptype': 'YouYiBao',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi K20 Pro Premium Edition Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 XWEB/2853 MMWEBSDK/20210601 Mobile Safari/537.36 MMWEBID/759 MicroMessenger/8.0.7.1920(0x28000737) Process/appbrand2 WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
    'content-type': 'application/json',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'token': token,
    'Referer': 'https://servicewechat.com/wx2756fa14246ce7a6/94/page-frame.html'
}
getUserRecordStatis_url = 'https://iot.universal-space.cn//api/mns/mnsGameStatis/getUserRecordStatis?productId=3160'
'''
{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "statisPage": "/pages/wacca/wacca-statis",
        "productImage": "https://static.universal-space.cn/images/20210225/1614238244-057dcd8807a598746053dfd049b76eeeW9kj2iIfL3P6in4TmlMMzqhnH1mQwN5p.jpg",
        "productId": 3160,
        "highestScore": 1000000,
        "recordPage": "/pages/wacca/wacca-detail",
        "userRank": 503,
        "totalCount": 392,
        "productName": "华卡音舞",
        "averageScore": 957725.9
    }
}
'''
getMemberInfo_url = 'https://iot.universal-space.cn//api/marv/wacca/getMemberInfo?'
'''
{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "memberType": 3,
        "validDays": 88,
        "vipCount": 95,
        "userLevel": 36,
        "userExp": 3575,
        "waccaPoint": 9999,
        "ticketCount": 3,
        "boostBadgeCount": 0,
        "boostBadgeSCount": 0,
        "trophyCount": 25,
        "unlockCount": 52,
        "titleCount": 30,
        "userName": "远哥制造",
        "userTitle": "坚持直到我觉得厌烦了",
        "iconUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/icon/102074.png",
        "iconName": "和服伊莉莎白",
        "iconRarity": 2,
        "memberFee": 2000
    }
}
'''
getUserTrophyStatis_url = 'https://iot.universal-space.cn//api/marv/wacca/getUserTrophyStatis?seasonId=1'
'''
{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "totalCount1": 6,
        "obtainCount3": 7,
        "obtainCount2": 6,
        "totalCount2": 7,
        "obtainCount4": 6,
        "obtainRate": 76,
        "obtainCount": 25,
        "totalCount": 33,
        "obtainCount1": 6,
        "totalCount3": 9,
        "totalCount4": 11
    }
}
'''
getTrophyList_url = 'https://iot.universal-space.cn//api/marv/wacca/getTrophyList?pageNo=1&pageSize=5&seasonId=1&trophyRarity=1'
'''
{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "pageNo": 1,
    "pageSize": 5,
    "totalPage": 1,
    "totalSize": 5,
    "data": [
        {
            "clearFlag": 1,
            "trophyUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/trophy/1-1.png",
            "clearDate": "2020-10-18 18:01:53",
            "trophyName": "脱离初学者行列",
            "targetValue": 10000,
            "description": "玩家达成等级5",
            "progress": 10000,
            "trophyType": 1,
            "trophyRarity": 1,
            "createDate": "2020-10-16 19:01:58"
        },
        {
            "clearFlag": 1,
            "trophyUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/trophy/2-1.png",
            "clearDate": "2020-11-15 10:25:44",
            "trophyName": "WACCA点数得分者",
            "targetValue": 10000,
            "description": "达成累积获得WP20000点数",
            "progress": 10000,
            "trophyType": 2,
            "trophyRarity": 1,
            "createDate": "2020-10-16 19:01:58"
        },
        {
            "clearFlag": 1,
            "trophyUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/trophy/2-1.png",
            "clearDate": "2020-10-25 18:42:06",
            "trophyName": "前往得分者的道路！",
            "targetValue": 10000,
            "description": "达成累积获得30000000点数",
            "progress": 10000,
            "trophyType": 2,
            "trophyRarity": 1,
            "createDate": "2020-10-16 19:01:58"
        },
        {
            "clearFlag": 1,
            "trophyUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/trophy/3-1.png",
            "clearDate": "2020-11-08 17:51:29",
            "trophyName": "持有称号",
            "targetValue": 10000,
            "description": "获得10个称号",
            "progress": 10000,
            "trophyType": 3,
            "trophyRarity": 1,
            "createDate": "2020-10-16 19:01:58"
        },
        {
            "clearFlag": 1,
            "trophyUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/trophy/3-1.png",
            "clearDate": "2020-10-25 17:24:42",
            "trophyName": "Icon爱好者",
            "targetValue": 10000,
            "description": "获得5个头像",
            "progress": 10000,
            "trophyType": 3,
            "trophyRarity": 1,
            "createDate": "2020-10-16 19:01:58"
        }
    ]
}
{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "pageNo": 1,
    "pageSize": 1,
    "totalPage": 1,
    "totalSize": 1,
    "data": [
        {
            "clearFlag": 1,
            "trophyUrl": "https://yyb-oss.universal-space.cn/imgs/wacca/trophy/3-1.png",
            "clearDate": "2020-11-08 17:51:29",
            "trophyName": "我的颜色爱好者",
            "targetValue": 10000,
            "description": "获得2个我的颜色",
            "progress": 10000,
            "trophyType": 3,
            "trophyRarity": 1,
            "createDate": "2020-10-16 19:01:58"
        }
    ]
}
'''
getUserTitleList_url = 'https://iot.universal-space.cn//api/marv/wacca/getUserTitleList?pageNo=1&pageSize=20&titleType=1'
'''
{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "pageNo": 1,
    "pageSize": 20,
    "totalPage": 1,
    "totalSize": 20,
    "data": [
        {
            "titleType": 1,
            "titleName": "您玩得好棒喔",
            "titleRarity": 3,
            "titleId": 10104011,
            "description": "达成ALL Marvelous"
        },
        {
            "titleType": 1,
            "titleName": "速度狂人",
            "titleRarity": 2,
            "titleId": 10104056,
            "description": "玩过50次超快速歌曲。"
        },
        {
            "titleType": 1,
            "titleName": "我好像有点强",
            "titleRarity": 1,
            "titleId": 10104052,
            "description": "玩家等级到达30。"
        },
        {
            "titleType": 1,
            "titleName": "我真的通关了「S」级以上",
            "titleRarity": 2,
            "titleId": 10104061,
            "description": "从HARD难易度达成100次S级的纪录"
        },
        {
            "titleType": 1,
            "titleName": "Vocaloid是我的偶像",
            "titleRarity": 2,
            "titleId": 10104019,
            "description": "游玩vocaloid的歌曲时，达成50次 S级的成绩。"
        },
        {
            "titleType": 1,
            "titleName": "我通过了SS级",
            "titleRarity": 3,
            "titleId": 10104006,
            "description": "从EXPERT难易度达成30次SS级的纪录"
        },
        {
            "titleType": 1,
            "titleName": "POP玩家",
            "titleRarity": 2,
            "titleId": 10104038,
            "description": "游玩动画/ 流行歌的歌曲时，达成50次 S级的成绩。"
        },
        {
            "titleType": 1,
            "titleName": "坚持直到我觉得厌烦了",
            "titleRarity": 2,
            "titleId": 10104057,
            "description": "连续10次游玩同一首歌曲。"
        },
        {
            "titleType": 1,
            "titleName": "我是爱动漫歌曲的御宅族",
            "titleRarity": 2,
            "titleId": 10104016,
            "description": "游玩动画/ 流行歌歌曲30次"
        },
        {
            "titleType": 1,
            "titleName": "初赛大成功",
            "titleRarity": 1,
            "titleId": 10104165,
            "description": "通过基本闸门10来获得"
        },
        {
            "titleType": 1,
            "titleName": "WACCA S关卡 VI过关!",
            "titleRarity": 2,
            "titleId": 10104154,
            "description": "升级关卡关卡VI通关"
        },
        {
            "titleType": 1,
            "titleName": "WACCA S关卡 V过关!",
            "titleRarity": 2,
            "titleId": 10104153,
            "description": "升级关卡关卡V通关"
        },
        {
            "titleType": 1,
            "titleName": "WACCA S关卡 I过关!",
            "titleRarity": 1,
            "titleId": 10104149,
            "description": "升级关卡关卡I通关"
        },
        {
            "titleType": 1,
            "titleName": "快点决定吧",
            "titleRarity": 1,
            "titleId": 10104058,
            "description": "试过5次重选歌曲才开始游玩。"
        },
        {
            "titleType": 1,
            "titleName": "我超爱Vocaloid",
            "titleRarity": 2,
            "titleId": 10104015,
            "description": "游玩vocaloid的歌曲30次。"
        },
        {
            "titleType": 1,
            "titleName": "HARDCORE好开森",
            "titleRarity": 2,
            "titleId": 10104018,
            "description": "游玩HARDCORE TANO*C的歌曲30次。"
        },
        {
            "titleType": 1,
            "titleName": "我的战斗现在才开始",
            "titleRarity": 2,
            "titleId": 10104054,
            "description": "玩过90次HARD以上的难易度。"
        },
        {
            "titleType": 1,
            "titleName": "我的等级终于到10啦",
            "titleRarity": 1,
            "titleId": 10104014,
            "description": "玩家等级到达10。"
        },
        {
            "titleType": 1,
            "titleName": "今天也来玩",
            "titleRarity": 1,
            "titleId": 10104164,
            "description": "通过基本闸门8来获得"
        },
        {
            "titleType": 1,
            "titleName": "为了与强者相遇而来",
            "titleRarity": 1,
            "titleId": 10104049,
            "description": "玩过1次多人模式(对战)。"
        }
    ]
}
'''
userMusicRate_url = 'https://iot.universal-space.cn//api/marv/wacca/userMusicRate?'
'''
{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "masterCount": 1,
        "fullcomboCount": 78,
        "rateSsCount": 167,
        "rateSssCount": 91,
        "clearCount": 387,
        "rateSCount": 111,
        "misslessCount": 269
    }
}
'''
recordDetail_url = 'https://iot.universal-space.cn//api/mns/mnsGame/recordDetail?machineId=8340&scoreId=1481655'
'''
{
    "code": 1,
    "message": "success",
    "detail": "success",
    "retCode": 0,
    "retMsg": "success",
    "data": {
        "scoreDetail": {
            "modeName": "单人模式",
            "comboCount": 141,
            "gameDate": "2021-07-09 17:53:28",
            "recordPage": "/pages/wacca/wacca-detail",
            "productName": "华卡音舞",
            "machineName": "华卡音舞",
            "score": 938818,
            "productImage": "https://static.universal-space.cn/images/20210225/1614238244-057dcd8807a598746053dfd049b76eeeW9kj2iIfL3P6in4TmlMMzqhnH1mQwN5p.jpg",
            "musicId": 20,
            "goodCount": 8,
            "storeName": "东方英雄（中央大道店）",
            "musicGrade": 3,
            "scoreId": 1481655,
            "statisPage": "/pages/wacca/wacca-statis",
            "productId": 3160,
            "musicRate": "S",
            "storeId": 4531,
            "greatCount": 61,
            "musicName": "MEMORiZE",
            "marvelousCount": 541,
            "machineId": 8340,
            "musicGradeName": "Expert",
            "artistName": "REDALiCE feat. Ayumi Nomiya",
            "musicImage": "https://yyb-oss.universal-space.cn/imgs/wacca/jacket/uT_J_S00_020.png",
            "missCount": 16
        },
        "getItems": {
            "titleList": [],
            "iconList": [],
            "trophyList": []
        }
    }
}
'''


def save_record_list():
    session = requests.Session()
    page = 1
    while True:
        url = f'https://iot.universal-space.cn//api/mns/mnsGame/recordList?productId=3160&pageNo={page}&pageSize=5&orderBy=gameDate'
        r = session.get(url, headers=headers, verify=False)
        r_json = r.json()
        if r_json['retCode'] == 0:
            data = r_json['data']
            for each in data:
                scoreId = each['scoreId']
                modeName = each['modeName']
                comboCount = each['comboCount']
                # productId = each['productId']
                musicRate = each['musicRate']
                gameDate = each['gameDate']
                storeId = each['storeId']
                greatCount = each['greatCount']
                # productName = each['productName']
                # machineName = each['machineName']
                musicName = each['musicName']
                score = each['score']
                marvelousCount = each['marvelousCount']
                machineId = each['machineId']
                musicId = each['musicId']
                goodCount = each['goodCount']
                musicGradeName = each['musicGradeName']
                storeName = each['storeName']
                artistName = each['artistName']
                musicGrade = each['musicGrade']
                musicImage = each['musicImage']
                missCount = each['missCount']
                cache_dt = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                if not Record.query.filter(Record.scoreId == scoreId).first():
                    new_wacca_Record = Record(scoreId, modeName, comboCount, musicRate, gameDate, storeId, greatCount,
                                              musicName, score, marvelousCount, machineId, musicId, goodCount,
                                              musicGradeName, storeName, artistName, musicGrade, musicImage, missCount,
                                              cache_dt)
                    new_wacca_Record.save()
        page += 1
        # TODO：out of cycle
