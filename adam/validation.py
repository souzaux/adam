# -*- coding: utf-8 -*-

"""
    adam.validation
    ~~~~~~~~~~~~~~~

    :copyright: (c) 2016 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""
from eve.io.mongo import Validator
import re


class Validator(Validator):
    def _validate_type_swift(self, field, value):
        """ Validate SWIFT/BIC bank codes """
        if not re.match('^[A-Z]{6}[A-Z0-9]{2}([A-Z0-9]{3})?$', value):
            self._error(field, 'Invalid SWIFT/BIC code.')

    def _validate_type_iban(self, field, value):
        """ Validate value bank numbers """

        if value is None:
            return

        if value.startswith('IT'):
            self._validate_italian_iban_number(field, value)
        else:
            self._error(field, 'Unsupported or unknown IBAN format.')

    def _validate_italian_iban_number(self, field, value):
        iban = value.replace(' ', '')

        if len(iban) != 27:
            self._error(field, 'Italian IBAN number should be 27 characters '
                        'long.')
            return

        if not re.match('^[A-Z0-9]', iban):
            self._error(field, 'Only characters and numbers allowed.')

        bank = iban[4:] + iban[:4]
        ascii_shift = 55

        s = ''
        for char in bank:
            v = ord(char) - ascii_shift if char.isalpha() else int(char)
            s += str(v)

        checksum = int(s[0])
        for i in range(1, len(s)):
            v = int(s[i])
            checksum *= 10
            checksum += v
            checksum %= 97

        if checksum != 1:
            self._error(field, 'Checksum mismatch for an Italian IBAN.')

    def _validate_type_tax_id_number(self, field, value):
        """ Validate fiscal code numbers """

        if value is None or value == '':
            self._error(field, 'Cannot be empty or null')
            return

        if len(value) == 11 and (value[0] == '8' or value[0] == '9'):
            self._validate_italian_vat_number(field, value)
            return

        if len(value) != 16:
            self._error(field,
                        'Italian tax id number should be 16 characters.')
            return

        value = value.upper()

        set1 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        set2 = "ABCDEFGHIJABCDEFGHIJKLMNOPQRSTUVWXYZ"
        even = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        odd = "BAKPLCQDREVOSFTGUHMINJWZYX"

        s = 0
        for i in range(1, 15, 2):
            s += even.index(set2[set1.index(value[i])])

        for i in range(0, 16, 2):
            s += odd.index(set2[set1.index(value[i])])

        if not (s % 26 == ord(value[15]) - 65):
            self._error(field, 'Invalid Italian tax id number.')

    def _validate_type_vat(self, field, value):
        """ Validate VAT numbers """

        if value.startswith('IT'):
            self._validate_italian_vat_number(field, value)
        else:
            self._error(field, 'Unsupported VAT number format.')

    def _validate_italian_vat_number(self, field, value):
        """ Validate Italian VAT numbers """

        value = value.lstrip('IT')
        if len(value) != 11:
            self._error(field, 'Italian VAT number must have 11 numeric '
                        'charactters.')
            return False

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
            self._error(field, 'Invalid Italian VAT number.')
            return False

        return True
