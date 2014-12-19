# -*- coding: utf-8 -*-
"""
    adam.domain.dashboard_documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    'dashboard_documents' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from collections import namedtuple
from adam.domain.dashboard.common import month_series, year, key as common_key
from adam.domain.common import base_def, base_schema

SchemaKey = namedtuple('SchemaKey', 'invoices, orders, year, company')
key = SchemaKey(
    invoices='i',
    orders='o',
    year=common_key.year,
    company=common_key.company
)

# TODO db index on company+year

url = 'dashboard-documents'

_schema = {
    key.year: year,
    key.invoices: month_series,                # invoices
    key.orders: month_series,                  # orders
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
