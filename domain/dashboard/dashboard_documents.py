# -*- coding: utf-8 -*-
"""
    adam.domain.dashboard_documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'dashboard_documents' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from domain.dashboard.common import month_series
from domain.common import base_def, base_schema, required_datetime


_year_series = {
    'type': 'dict',
    'required': True,
    'schema': {
        'c': month_series,             # current year
        'p': month_series,             # previous year
    },
}

_schema = {
    'y': required_datetime,             # current year
    'b': _year_series,                  # billed
    'o': _year_series,                  # orders
    }
_schema.update(base_schema)

definition = {
    'url': 'dashboard-documents',
    'item_title': 'documents dashboard',
    'schema': _schema,
}
definition.update(base_def)
