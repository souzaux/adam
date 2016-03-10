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

        valid = [
            'IT01180680397',
            'IT02182030391',
            'IT92078790398'
        ]
        for challenge in valid:
            self.assertTrue(self.validator({'vat': challenge}))

        invalid = [
            '01180680397',
            'UK01180680397',
            'IT1234567890',
            'A'
        ]
        for challenge in invalid:
            self.assertFalse(self.validator({'vat': challenge}))

    def test_tax_id_number_validation(self):
        self.validator.schema = {'id': {'type': 'tax_id_number'}}

        valid = [
            'RCCNCL70M27B519E',
            'grdsfn66d17h199k',
            '92078790398',
            '95052810132',
            '94078890541',
            '90029830669',
            '81004300067',
            '80064390372',
            '80028050583',
            '80007770102',
            '80003350891'
        ]
        for challenge in valid:
            self.assertTrue(self.validator({'id': challenge}))

        invalid = [
            None,
            'A',
            '12345678901234567'
        ]
        for challenge in invalid:
            self.assertFalse(self.validator({'id': challenge}))

    def test_iban_validation(self):
        self.validator.schema = {'iban': {'type': 'iban'}}

        valid = [
            'IT88T1927501600CC0010110180',
            'IT 88T 19275016 00CC001 0110180',
        ]
        for challenge in valid:
            self.assertTrue(self.validator({'iban': challenge}))

        invalid = [
            None,
            '',
            'ABC',
            '88T1927501600CC0010110180'
        ]
        for challenge in invalid:
            self.assertFalse(self.validator({'iban': challenge}))

    def test_swift_validation(self):
        self.validator.schema = {'swift': {'type': 'swift'}}

        valid = [
            'ABCOITMM',
            'ICRAITRRL90',
            'CRGEITGG183'
        ]
        for challenge in valid:
            self.assertTrue(self.validator({'swift': challenge}))

        invalid = [
            '',
            'ABC',
            '12345678901'
        ]
        for challenge in invalid:
            self.assertFalse(self.validator({'swift': challenge}))
