# -*- coding: utf-8 -*-
"""
    adam.run-production.py
    ~~~~~~~~~~~~~~~~~~~~~~

    Production script sample, using Tornado.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from run import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
IOLoop.instance().start()
