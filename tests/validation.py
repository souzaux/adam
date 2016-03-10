# -*- coding: utf-8 -*-
"""
    adam.tests.validation.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Test adam custom validation.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""

from adam.validation import Validator
from unittest import TestCase


class TestValidator(TestCase):
    def setUp(self):
        super(TestValidator, self).setUp()
        self.validator = Validator()

    def test_vat_validation(self):
        self.validator.schema = {'vat': {'type': 'vat'}}

        self.assertTrue(self.validator({'vat': 'IT01180680397'}))
        self.assertTrue(self.validator({'vat': 'IT02182030391'}))
        self.assertTrue(self.validator({'vat': 'IT92078790398'}))

        self.assertFalse(self.validator({'vat': '01180680397'}))
        self.assertFalse(self.validator({'vat': 'UK01180680397'}))
        self.assertFalse(self.validator({'vat': 'IT1234567890'}))
        self.assertFalse(self.validator({'vat': 'A'}))
