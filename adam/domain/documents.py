# -*- coding: utf-8 -*-
"""
    adam.domain.documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'documents' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from common import base_def, base_schema, required_datetime, required_integer

total_key = 't'
date_key = 'd'

url = 'documents'

_schema = {
    date_key: required_datetime,             # docment date
    total_key: required_integer              # total amount
    }
_schema.update(base_schema)

definition = {
    'url': url,
    'schema': _schema,
}
definition.update(base_def)
