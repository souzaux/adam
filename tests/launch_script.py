# -*- coding: utf-8 -*-
"""
    adam.tests.launch_script.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test adam launch script.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os
from eve import Eve
from . import TestBase, run


class TestLaunchScript(TestBase):
    def test_app(self):
        self.assertIsInstance(self.app, Eve)

    def test_local_host(self):
        try:
            del(os.environ['PORT'])
        except KeyError:
            pass
        reload(run)
        self.assertEqual(run.host, '127.0.0.1')
        self.assertEqual(run.port, 5000)

    def test_heroku_host(self):
        os.environ['PORT'] = '12345'
        reload(run)
        self.assertEqual(run.host, '0.0.0.0')
        self.assertEqual(run.port, 12345)
