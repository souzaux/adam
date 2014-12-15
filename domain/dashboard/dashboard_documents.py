# -*- coding: utf-8 -*-
"""
    adam.domain.dashboard_documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'dashboard_documents' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from domain.dashboard.common import month_series, year
from domain.common import base_def, base_schema

# TODO db index on company+year

_schema = {
    'y': year,
    'b': month_series,                  # billed
    'o': month_series,                  # orders
    }
_schema.update(base_schema)

definition = {
    'url': 'dashboard-documents',
    'item_title': 'documents dashboard',
    'datasource': {'source': 'dashboard_documents'},
    'schema': _schema,
}
definition.update(base_def)
