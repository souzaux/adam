# -*- coding: utf-8 -*-
"""
    adam.tests
    ~~~~~~~~~~

    Just providing code coverage for Adam's own functionality. Eve's rich
    test suite takes care of all the API logic.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os
import unittest

from flask.ext.pymongo import MongoClient

MONGO_DBNAME = 'adam_test'
MONGO_USERNAME = 'test_user'
MONGO_PASSWORD = 'test_pw'
MONGO_HOST = 'localhost'
MONGO_PORT = 27017

# black magic
os.environ['TESTING'] = 'True'
import sys; sys.path.insert(0, '../'); import run  # noqa


class TestBase(unittest.TestCase):
    def setUp(self):
        """ Prepare the test fixture """

        self.setupDB()

        self.app = run.app
        self.domain = self.app.config['DOMAIN']

        self.test_client = self.app.test_client()

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
        user_accounts = [
            {'u': 'app@gmail.com', 'p': 'pw1', 't': 'token1', 'r': ['app']},
            {'u': 'user@gmail.com', 'p': 'pw1', 't': 'token2', 'r': ['user']},
        ]
        _db = self.connection[MONGO_DBNAME]
        _db.user_accounts.insert(user_accounts)
        self.connection.close()

    def dropDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        self.connection.close()
