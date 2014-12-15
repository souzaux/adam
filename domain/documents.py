# -*- coding: utf-8 -*-
"""
    adam.domain.documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'documents' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from domain.common import base_def, base_schema, required_datetime, \
    required_integer


_schema = {
    'd': required_datetime,             # docment date
    't': required_integer               # total amount
    }
_schema.update(base_schema)

definition = {
    'schema': _schema,
}
definition.update(base_def)
