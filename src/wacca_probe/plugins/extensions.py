#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/12 23:33
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""
from flask_sqlalchemy import SQLAlchemy

from flask_compress import Compress

db = SQLAlchemy()
compress = Compress()
