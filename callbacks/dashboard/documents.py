# -*- coding: utf-8 -*-
"""
    callbacks.dashboard.documents.insert.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Dashboard Insertion Module.

    This module updates the dashboard each time a document which is relevant
    to the dashboard is added to the server.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from flask import current_app as app

from domain.common import company_key
from domain.documents import total_key
from domain.dashboard.common import year_key, amount_key, quantity_key
from domain.dashboard.dashboard_documents import invoices_key, orders_key

import datetime  # noqa


def documents_insert(docs):
    """ Documents have been inserted; update dashboard accordingly """

    for doc in docs:
        _dashboard_update(doc, doc[total_key], 1)


def document_replace(new, original):
    """ Document has been replaced; update dashboard accordingly """

    delta = new[total_key] - original[total_key]
    _dashboard_update(new, delta, 0)


def _dashboard_update(doc, amount, quantity):
    """ Updates a documents dashboard """

    date = doc['d']
    year, month = date.year, date.month-1

    company = doc[company_key]
    lookup = {company_key: company, year_key: year}

    array = [{amount_key: 0, quantity_key: 0} for k in range(12)]
    empty = {company_key: company, year_key: year, invoices_key: array,
             orders_key: array}

    # add auth_field if needed
    resource_def = app.config['DOMAIN']['documents']
    auth = resource_def['authentication']
    auth_field = resource_def['auth_field']
    if auth and auth_field:
        auth_value = auth.get_request_auth_value()
        empty.update({auth_field: auth_value})

    # TODO conditional set based on actual doc_type
    doc_type = invoices_key

    dashboard = app.data.driver.db['dashboard_documents']

    bulk = dashboard.initialize_ordered_bulk_op()

    # add dashboard if needed
    bulk.find(lookup).upsert().update({'$setOnInsert': empty})

    # update dashboard
    item = '%s.%d' % (doc_type, month)
    amount_item = '%s.%s' % (item, amount_key)
    quantity_item = '%s.%s' % (item, quantity_key)
    bulk.find(lookup).update({'$inc': {amount_item: amount, quantity_item:
                                       quantity}})
    r = bulk.execute()

    # TODO remove or log?
    if app.config['DEBUG'] is True:
        from pprint import pprint
        pprint(r)
