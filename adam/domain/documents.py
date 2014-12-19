# -*- coding: utf-8 -*-
"""
    adam.domain.documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'documents' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple
from common import base_def, base_schema, required_datetime, required_integer,\
    key as common_key

SchemaKey = namedtuple('SchemaKey', 'company, total, date, type')
key = SchemaKey(
    company=common_key.company,
    total=common_key.total,
    date=common_key.date,
    type=common_key.type
)

DocumentTypes = namedtuple('DocumentTypes', 'customer_order, invoice')

doctype = DocumentTypes(
    customer_order='co',
    invoice='i'
)


url = 'documents'

_schema = {
    key.date: required_datetime,             # docment date
    key.total: required_integer,             # total amount
    key.type: {
        'type': 'string',
        'allowed': doctype._asdict().values(),
        'required': True
    }
}
_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
}
definition.update(base_def)
