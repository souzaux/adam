# -*- coding: utf-8 -*-
"""
    adam.domain.dashboard_documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'dashboard_documents' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from adam.domain.dashboard.common import month_series, year, year_key
from adam.domain.common import base_def, base_schema

# TODO db index on company+year
invoices_key = 'i'
orders_key = 'o'

url = 'dashboard-documents'

_schema = {
    year_key: year,
    invoices_key: month_series,                # invoices
    orders_key: month_series,                  # orders
}
_schema.update(base_schema)

definition = {
    'url': url,
    'item_title': 'documents dashboard',
    'datasource': {'source': 'dashboard_documents'},
    'resource_methods': ['GET'],
    'item_methods': ['GET'],
    'schema': _schema,
}
definition.update(base_def)
