#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/13 19:29
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""
import flask

from wacca_probe import cache
from wacca_probe.models.wacca import Record

app = flask.current_app
bp = flask.Blueprint('main', __name__)


@bp.route('/')
@cache.cached()
def site_index():
    return flask.render_template('index.html')


@bp.route('/record')
@cache.cached()
def record():
    page = int(flask.request.args.get('page', 1))
    per_page = int(flask.request.args.get('per_page', 20))
    if 'all' in flask.request.args:
        per_page = 10000
    if 'artistName' in flask.request.args:
        _artistName = flask.request.args.get('artistName')
        record_data_paginate = Record.query.filter_by(artistName=_artistName) \
            .order_by(Record.id.desc()) \
            .paginate(page, per_page)
    else:
        record_data_paginate = Record.query.order_by(Record.id.desc()).paginate(page, per_page)
    # total = record_data_paginate.total
    # total_page = math.ceil(total / per_page)
    return flask.render_template('wacca/record/list.html', record_data_paginate=record_data_paginate,
                                 page=page, per_page=per_page)


@bp.route('/test')
def test():
    import json
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
            if not Record.query.filter(Record.scoreId == scoreId).first():
                new_wacca_Record = Record(scoreId, modeName, comboCount, musicRate, gameDate, storeId, greatCount,
                                          musicName, score, marvelousCount, machineId, musicId, goodCount,
                                          musicGradeName, storeName, artistName, musicGrade, musicImage, missCount)
                r = new_wacca_Record.save()
                print(r)
            else:
                print(f'scoreId {scoreId} 已存在')
    return '1'
