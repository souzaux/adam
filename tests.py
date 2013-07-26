# -*- coding: utf-8 -*-
"""
    adam.tests.py
    ~~~~~~~~~~~~

    Just providing code coverage for Adam's own functionality. Eve's rich
    test suite takes care of all the API logic.

    For launching the suite just run: `python -m unittest tests`.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os
import unittest
from eve import Eve
from flask.ext.pymongo import MongoClient
import run

MONGO_DBNAME = 'adam_test'
MONGO_USERNAME = 'test_user'
MONGO_PASSWORD = 'test_pw'
MONGO_HOST = 'localhost'
MONGO_PORT = 27017


class TestBase(unittest.TestCase):
    def setUp(self):
        if 'PORT' in os.environ:
            # cleanup
            del(os.environ['PORT'])


class TestMinimal(TestBase):
    def setUp(self):
        """ Prepare the test fixture
        """
        self.setupDB()
        super(TestMinimal, self).setUp()
        self.app = Eve(settings='settings.py', auth=run.Auth)
        self.test_client = self.app.test_client()
        self.domain = self.app.config['DOMAIN']

    def tearDown(self):
        self.dropDB()

    def assert200(self, status):
        self.assertEqual(status, 200)

    def assert301(self, status):
        self.assertEqual(status, 301)

    def assert404(self, status):
        self.assertEqual(status, 404)

    def assert304(self, status):
        self.assertEqual(status, 304)

    def assert400(self, status):
        self.assertEqual(status, 400)

    def assert401(self, status):
        self.assertEqual(status, 401)

    def assert401or405(self, status):
        self.assertTrue(status == 401 or 405)

    def assert403(self, status):
        self.assertEqual(status, 403)

    def assert405(self, status):
        self.assertEqual(status, 405)

    def assert412(self, status):
        self.assertEqual(status, 412)

    def assert500(self, status):
        self.assertEqual(status, 500)

    def setupDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        if MONGO_USERNAME:
            self.connection[MONGO_DBNAME].add_user(MONGO_USERNAME,
                                                   MONGO_PASSWORD)
        self.bulk_insert()

    def bulk_insert(self):
        accounts = [
            {'u': 'app@gmail.com', 'p': 'pw1', 't': 'token1', 'r': ['app']},
            {'u': 'user@gmail.com', 'p': 'pw1', 't': 'token2', 'r': ['user']},
        ]
        _db = self.connection[MONGO_DBNAME]
        _db.accounts.insert(accounts)
        self.connection.close()

    def dropDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        self.connection.close()


class TestAuth(TestMinimal):
    """ We rely on Eve's own test suite. Here we're just testing Adam
    functionality.
    """
    def setUp(self):
        super(TestAuth, self).setUp()
        self.valid_auth = [('Authorization', 'Basic dG9rZW4xOg==')]
        self.invalid_auth = [('Authorization', 'Basic IDontThinkSo')]

    def test_valid_access(self):
        r = self.test_client.get('/', headers=self.valid_auth)
        self.assert200(r.status_code)

    def test_invalid_access(self):
        r = self.test_client.get('/', headers=self.invalid_auth)
        self.assert401(r.status_code)


class TestHost(TestBase):
    def test_local_host(self):
        reload(run)
        self.assertTrue(run.host is None)
        self.assertTrue(run.port == 5000)

    def test_heroku_host(self):
        os.environ['PORT'] = '12345'
        reload(run)
        self.assertTrue(run.host == '0.0.0.0')
        self.assertTrue(run.port == 12345)


class TestEve(TestBase):
    def test_eve(self):
        reload(run)
        self.assertTrue(type(run.app) is Eve)
