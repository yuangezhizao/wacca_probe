#!/usr/bin/env/ python3
# -*- coding: utf-8 -*-
"""
    :Author: yuangezhizao
    :Time: 2021/7/12 21:08
    :Site: https://www.yuangezhizao.cn
    :Copyright: © 2021 yuangezhizao <root@yuangezhizao.cn>
"""
import os
import time

import flask

from config import config


class ReverseProxied(object):
    # Flask url_for generating http URL instead of https
    # https://stackoverflow.com/questions/14810795/flask-url-for-generating-http-url-instead-of-https

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        scheme = environ.get('HTTP_X_API_SCHEME')
        if scheme:
            environ['wsgi.url_scheme'] = scheme
        return self.app(environ, start_response)


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'production')

    app = flask.Flask(__name__, static_url_path='', instance_relative_config=True)
    app.wsgi_app = ReverseProxied(app.wsgi_app)

    app.config.from_object(config[config_name])
    app.config.from_pyfile(f'{config_name}.py')

    register_extensions(app)
    register_blueprints(app)
    register_template_context(app)

    return app


def register_extensions(app):
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    from wacca_probe.plugins.extensions import db, compress

    db.init_app(app)
    compress.init_app(app)


def register_blueprints(app):
    from wacca_probe.views import register_views
    register_views(app)


def register_template_context(app):
    @app.before_request
    def before_request():
        flask.g.start_time = time.time()

    @app.after_request
    def after_request(response):
        if ('Content-Length' in response.headers):
            response.headers.add('Uncompressed-Content-Length', response.headers['Content-Length'])
        start_to_stop_time = time.time() - flask.g.start_time
        response.headers.add('Response-Time', round(start_to_stop_time, 3))
        return response

    @app.template_filter('my_split')
    def my_split(this, string, num):
        return str(this).split(string)[num]