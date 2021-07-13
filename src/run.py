#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/13 19:34
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""
from wacca_probe import create_app

flask_app = create_app()

if __name__ == '__main__':
    flask_app.run(host='127.0.0.1', port=4000, threaded=True)
