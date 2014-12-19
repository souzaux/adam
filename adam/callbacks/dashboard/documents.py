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
import os

from flask import current_app as app

import adam.domain.documents as docs
from adam.domain.dashboard.common import key as months_key
from adam.domain.dashboard.dashboard_documents import key

from adam.callbacks.common import auth

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


def documents_insert(documents):
    """ Documents have been inserted; update dashboard accordingly """

    for doc in documents:
        delta = doc[docs.key.total]
        _dashboard_update(delta, 1, *_meta(doc))


def document_replace(new, original):
    """ Document has been replaced; update dashboard accordingly """

    delta = new[docs.key.total] - original[docs.key.total]
    _dashboard_update(delta, 0, *_meta(new))


def document_delete(doc):
    """ Document has been deleted; update dashboard accordingly """
    delta = doc[docs.key.total] * -1
    _dashboard_update(delta, -1, *_meta(doc))


def _meta(doc):
    """ Return document date and company """
    return doc[docs.key.date], doc[docs.key.company], doc[docs.key.type]


def _dashboard_update(delta, quantity, date, company, type):
    """ Updates a documents dashboard """

    year, month = date.year, date.month-1
    lookup = {key.company: company, key.year: year}

    array = [{months_key.amount: 0, months_key.quantity: 0} for k in range(12)]
    empty = {key.company: company, key.year: year, key.invoices: array,
             key.orders: array}

    auth_field, auth_value = auth('documents')
    if auth_value:
        empty.update({auth_field: auth_value})

    if type == docs.doctype.invoice:
        doc_type = key.invoices
    elif type == docs.doctype.customer_order:
        doc_type = key.orders

    dashboard = app.data.driver.db['dashboard_documents']

    bulk = dashboard.initialize_ordered_bulk_op()

    # add dashboard if needed
    bulk.find(lookup).upsert().update({'$setOnInsert': empty})

    # update dashboard
    item = '%s.%d' % (doc_type, month)
    amount_item = '%s.%s' % (item, months_key.amount)
    quantity_item = '%s.%s' % (item, months_key.quantity)
    bulk.find(lookup).update({'$inc': {amount_item: delta, quantity_item:
                                       quantity}})
    r = bulk.execute()

    # TODO remove or log?
    if app.config['DEBUG'] is True and os.environ.get('TESTING') is None:
        from pprint import pprint
        pprint(r)
