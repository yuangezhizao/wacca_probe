#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/13 19:29
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""
import flask

app = flask.current_app
bp = flask.Blueprint('main', __name__)


@bp.route('/test')
def test():
    import json
    import datetime
    from wacca_probe.plugins.extensions import db
    from wacca_probe.models.wacca import Record

    db.create_all()

    with open('wacca_probe/static/static/json/recordList.json', encoding='utf-8') as f:
        record = f.read()
        record_json = json.loads(record)
        data = record_json['data']
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
            cache_dt = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            if not Record.query.filter(Record.scoreId == scoreId).first():
                new_wacca_Record = Record(scoreId, modeName, comboCount, musicRate, gameDate, storeId, greatCount,
                                          musicName, score, marvelousCount, machineId, musicId, goodCount,
                                          musicGradeName, storeName, artistName, musicGrade, musicImage, missCount,
                                          cache_dt)
                r = new_wacca_Record.save()
                print(r)
            else:
                print(f'scoreId {scoreId} 已存在')
    return '1'
