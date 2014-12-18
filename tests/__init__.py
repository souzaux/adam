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
import simplejson as json
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
        self.valid_auth = [('Authorization', 'Basic dG9rZW4xOg==')]
        self.headers = [('Content-Type', 'application/json')] + self.valid_auth

    def tearDown(self):
        self.dropDB()

    def assert200(self, status):
        self.assertEqual(status, 200)

    def assert201(self, status):
        self.assertEqual(status, 201)

    def assert204(self, status):
        self.assertEqual(status, 204)

    def setupDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        if MONGO_USERNAME:
            self.connection[MONGO_DBNAME].add_user(MONGO_USERNAME,
                                                   MONGO_PASSWORD)
        db = self.connection[MONGO_DBNAME]
        self.accounts_insert(db)
        self.company_insert(db)
        db.connection.close()

    def accounts_insert(self, db):
        user_accounts = [
            {'u': 'app@gmail.com', 'p': 'pw1', 't': 'token1', 'r': ['app']},
            {'u': 'user@gmail.com', 'p': 'pw1', 't': 'token2', 'r': ['user']},
        ]
        db.user_accounts.insert(user_accounts)

    def company_insert(self, db):
        company = {'n': 'test_company', 'p': 'pw1'}
        self.company_id = str(db.companies.insert(company))

    def dropDB(self):
        self.connection = MongoClient(MONGO_HOST, MONGO_PORT)
        self.connection.drop_database(MONGO_DBNAME)
        self.connection.close()

    def post(self, url, payload):
        r = self.test_client.post(url, data=json.dumps(payload),
                                  headers=self.headers)
        return self.parse_response(r)

    def put(self, url, payload, etag):
        headers = self.headers + [('If-Match', etag)]
        r = self.test_client.put(url, data=json.dumps(payload),
                                 headers=headers)
        return self.parse_response(r)

    def delete(self, url, etag):
        headers = self.headers + [('If-Match', etag)]
        r = self.test_client.delete(url, headers=headers)
        return self.parse_response(r)

    def get(self, url):
        r = self.test_client.get(url, headers=self.headers)
        return self.parse_response(r)

    def parse_response(self, r):
        try:
            v = json.loads(r.get_data())
        except json.JSONDecodeError:
            v = None
        return v, r.status_code
