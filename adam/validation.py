# -*- coding: utf-8 -*-

"""
    adam.validation
    ~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""
from eve.io.mongo import Validator


class Validator(Validator):
    def _validate_type_vat(self, field, value):
        """ Validate VAT numbers """

        if value.startswith('IT'):
            self._validate_italian_vat_number(field, value)
        else:
            self._error(field, "Unsupported VAT number format.")

    def _validate_italian_vat_number(self, field, value):
        """ Validate Italian VAT numbers """

        value = value.lstrip('IT')
        if len(value) != 11:
            self._error(field, "Italian VAT number must have 11 numeric "
                        "charactters.")
            return

        tot = 0
        for i in range(0, 10, 2):
            tot += int(value[i])

        for i in range(1, 10, 2):
            odd = int(value[i])*2
            odd = (odd / 10) + (odd % 10)
            tot += odd

        checksum = int(value[10])

        if not ((tot % 10 == 0 and checksum == 0) or
                (10 - (tot % 10) == checksum)):
            self._error(field, "Invalid Italian VAT number.")
