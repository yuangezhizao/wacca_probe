#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/12 21:09
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""

import requests

from wacca_probe.models.wacca import Record

session = requests.Session()

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


def save_record_list():
    page = 1
    while True:
        url = f'https://iot.universal-space.cn//api/mns/mnsGame/recordList?productId=3160&pageNo={page}&pageSize=50&orderBy=gameDate'
        r = session.get(url, headers=headers, verify=False)
        r_json = r.json()
        if r_json['totalSize'] == 0:
            break
        data = r_json['data']
        record_count = len(data)
        for i in range(record_count - 1, -1, -1):
            scoreId = data[i]['scoreId']
            modeName = data[i]['modeName']
            comboCount = data[i]['comboCount']
            # productId = data[i]['productId']
            musicRate = data[i]['musicRate']
            gameDate = data[i]['gameDate']
            storeId = data[i]['storeId']
            greatCount = data[i]['greatCount']
            # productName = data[i]['productName']
            # machineName = data[i]['machineName']
            musicName = data[i]['musicName']
            score = data[i]['score']
            marvelousCount = data[i]['marvelousCount']
            machineId = data[i]['machineId']
            musicId = data[i]['musicId']
            goodCount = data[i]['goodCount']
            musicGradeName = data[i]['musicGradeName']
            storeName = data[i]['storeName']
            artistName = data[i]['artistName']
            musicGrade = data[i]['musicGrade']
            musicImage = data[i]['musicImage']
            missCount = data[i]['missCount']
            if not Record.query.filter(Record.scoreId == scoreId).first():
                new_wacca_Record = Record(scoreId, modeName, comboCount, musicRate, gameDate, storeId, greatCount,
                                          musicName, score, marvelousCount, machineId, musicId, goodCount,
                                          musicGradeName, storeName, artistName, musicGrade, musicImage, missCount)
                r = new_wacca_Record.save()
                print(r)
            else:
                print(f'scoreId {scoreId} 已存在')
        break  # 确保每次新增小于 50 次记录即可
        # page += 1
