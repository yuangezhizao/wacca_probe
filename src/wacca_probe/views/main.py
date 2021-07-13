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
    with open('static/static/json/recordList.json', encoding='utf-8') as f:
        data = f.read()
    return flask.jsonify(data)
