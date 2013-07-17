# -*- coding: utf-8 -*-
"""
    adam.tests.py
    ~~~~~~~~~~~~

    Just providing code coverage for Adam's own functionality. Eve's rich
    test suite takes care of all the API logic.

    For launching the suite, just run: `python -m unittest tests`.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import unittest
import run
import os
from eve import Eve


class TestBase(unittest.TestCase):
    def setUp(self):
        if 'PORT' in os.environ:
            # cleanup
            del(os.environ['PORT'])


class TestAuth(TestBase):
    """ We rely on Eve's own test suite. Here we're just testing Adam
    functionality.
    """
    def setUp(self):
        super(TestAuth, self).setUp()
        self.auth = run.Auth()
        if 'AUTH_USERNAME' in os.environ:
            # not strictly necessary but..
            del(os.environ['AUTH_USERNAME'])
            del(os.environ['AUTH_PASSWORD'])

    def test_local_auth_fail(self):
        self.assertFalse(self.auth.check_auth("itsme", "mypw", None, None))

    def test_local_auth_success(self):
        self.assertTrue(self.auth.check_auth("username", "password", None,
                                             None))

    def test_hosted_auth_success(self):
        os.environ['PORT'] = 'yeah'
        os.environ['AUTH_USERNAME'] = 'env_user'
        os.environ['AUTH_PASSWORD'] = 'env_password'
        self.assertTrue(self.auth.check_auth("env_user", "env_password", None,
                                             None))

    def test_hosted_auth_fail(self):
        os.environ['PORT'] = 'yeah'
        os.environ['AUTH_USERNAME'] = 'env_user'
        os.environ['AUTH_PASSWORD'] = 'env_password'
        self.assertFalse(self.auth.check_auth("itsme", "pw", None, None))


class TestHost(TestBase):
    def test_local_host(self):
        reload(run)
        self.assertTrue(run.host is None)
        self.assertTrue(run.port == 5000)

    def test_heroku_host(self):
        os.environ['PORT'] = '12345'
        reload(run)
        self.assertTrue(type(run.app) is Eve)
        self.assertTrue(run.host == '0.0.0.0')
        self.assertTrue(run.port == 12345)


class TestEve(TestBase):
    def test_eve(self):
        self.assertTrue(type(run.app) is Eve)
