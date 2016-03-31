# -*- coding: utf-8 -*-
"""
    adam.domain.payment.py
    ~~~~~~~~~~~~~~~~~~~~~~

    'payments' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import copy

from common import base_def, base_schema, topology, required_string, \
    required_integer, bank, unique_string
from fees import schema as fee_schema
from payment_methods import schema as payment_schema


url = topology.payments

_first_payment_option = {
    'type': 'dict',
    'required': True,
    'schema': {
        'code': required_integer,
        'description': required_string
    }
}

payment_bank = copy.deepcopy(bank)
payment_bank['required'] = False

_schema = {
    'name': unique_string,
    'discount': {'type': 'float'},
    'installments_every_number_of_days': {'type': 'integer'},
    'installments': {'type': 'integer'},
    'force_end_of_month': {'type': 'boolean'},
    'extra_days': {'type': 'integer'},
    'exact_days': {'type': 'integer'},
    'first_payment_date': _first_payment_option,
    'first_payment_option': _first_payment_option,
    'first_payment_additional_days': {'type': 'integer'},
    'bank': payment_bank,
    'payment_method': {
        'type': 'dict',
        'schema': payment_schema
    },
    'fee': {
        'type': 'dict',
        'schema': fee_schema,
    }
}

_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
}
definition.update(base_def)
