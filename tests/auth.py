# -*- coding: utf-8 -*-
"""
    adam.tests.auth.py
    ~~~~~~~~~~~~~~~~~~

    Test adam authentication scheme.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""

from . import TestBase
from adam.domain import documents as docs


class TestAuth(TestBase):
    def setUp(self):
        super(TestAuth, self).setUp()
        self.valid_auth = [('Authorization', 'Basic dG9rZW4xOg==')]
        self.invalid_auth = [('Authorization', 'Basic IDontThinkSo')]

    def test_valid_access(self):
        r = self.test_client.get('/%s' % docs.url, headers=self.valid_auth)
        self.assert200(r.status_code)

    def test_invalid_access(self):
        r = self.test_client.get('/%s' % docs.url, headers=self.invalid_auth)
        self.assert401(r.status_code)
