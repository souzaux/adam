# -*- coding: utf-8 -*-
"""
    adam.domain.documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'documents' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple
from common import base_def, base_schema, required_datetime, required_integer

total_key = 't'
date_key = 'd'
type_key = 'dt'

DocumentTypes = namedtuple('DocumentTypes', 'customer_order, invoice')

types = DocumentTypes(
    customer_order='co',
    invoice='i'
)


url = 'documents'

_schema = {
    date_key: required_datetime,             # docment date
    total_key: required_integer,             # total amount
    type_key: {
        'type': 'string',
        'allowed': types._asdict().values(),
        'required': True
    }
}
_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
}
definition.update(base_def)
