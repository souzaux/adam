# -*- coding: utf-8 -*-
"""
    callbacks.dashboard.documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Documents (invoices and orders) dashboard.

    This module updates the dashboard each time an invoice or an order
    is added, updated or delete.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from flask import current_app as app

from domain.common import company_key
from domain.documents import total_key, date_key
from domain.dashboard.common import year_key, amount_key, quantity_key
from domain.dashboard.dashboard_documents import invoices_key, orders_key

from callbacks.common import auth

import datetime  # noqa

""" IMPORTANT

    Since the dashboard is supposed to be readonly for the clients and we
    also want to strive for best performance since it will be updated
    frequently, we choose to udpate it out-of-band (not via internal Eve
    methods like 'post_internal').

    Side effect is that some meta fields like _updated and _created are
    not going to be reliable (_etag will be computed by eve on the fly
    since missing).
"""


def documents_insert(docs):
    """ Documents have been inserted; update dashboard accordingly """

    for doc in docs:
        delta = doc[total_key]
        _dashboard_update(delta, 1, *_meta(doc))


def document_replace(new, original):
    """ Document has been replaced; update dashboard accordingly """

    delta = new[total_key] - original[total_key]
    _dashboard_update(delta, 0, *_meta(new))


def document_delete(doc):
    """ Document has been deleted; update dashboard accordingly """
    delta = doc[total_key] * -1
    _dashboard_update(delta, -1, *_meta(doc))


def _meta(doc):
    """ Return document date and company """
    return doc[date_key], doc[company_key]


def _dashboard_update(delta, quantity, date, company):
    """ Updates a documents dashboard """

    year, month = date.year, date.month-1
    lookup = {company_key: company, year_key: year}

    array = [{amount_key: 0, quantity_key: 0} for k in range(12)]
    empty = {company_key: company, year_key: year, invoices_key: array,
             orders_key: array}

    auth_field, auth_value = auth('documents')
    if auth_value:
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
    bulk.find(lookup).update({'$inc': {amount_item: delta, quantity_item:
                                       quantity}})
    r = bulk.execute()

    # TODO remove or log?
    if app.config['DEBUG'] is True:
        from pprint import pprint
        pprint(r)
