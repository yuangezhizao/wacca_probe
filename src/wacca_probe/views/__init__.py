#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/13 19:29
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""


def register_views(flask_app):
    """ Register the blueprints using the flask_app object """
    from wacca_probe.views import (
        main,
    )
    flask_app.register_blueprint(main.bp)
