#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/13 21:24
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""
import severless_wsgi
from wacca_probe import create_app  # Replace with your actual application


# If you need to send additional content types as text, add then directly
# to the whitelist:
#
# serverless_wsgi.TEXT_MIME_TYPES.append("application/custom+json")

def handler(event, context):
    return severless_wsgi.handle_request(create_app(), event, context)
