# -*- coding: utf-8 -*-
"""
    adam.domain.payment_options.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'payment_methods' resource and schema settings.

    :copyright: (c) 2016 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import base_def, base_schema, topology, required_string


url = topology.payment_options

_modalita_pa = {
    'type': 'dict',
    'schema': {
        'code': required_string,
        'description': required_string
    }
}

_schema = {
    'name': required_string,
    'is_bank_receipt': {'type': 'boolean'},
    'pagamento_pa': _modalita_pa,
}

_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
}
definition.update(base_def)
