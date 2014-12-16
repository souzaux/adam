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
    """ Document has been inserted so we have to update the dashboard """
    for doc in docs:

        date = doc['d']
        year, month = date.year, date.month-1
        company = doc[company_key]

        # TODO consider adding auth_field to the lookup. Should not be
        # needed since year+cpmpany-key is unique
        lookup = {company_key: company, year_key: year}

        array = [{amount_key: 0, quantity_key: 0} for k in range(12)]
        empty = {
            company_key: company,
            year_key: year,
            invoices_key: array,
            orders_key: array
        }

        # add auth_field if needed
        resource_def = app.config['DOMAIN']['documents']
        auth = resource_def['authentication']
        auth_field = resource_def['auth_field']
        if auth and auth_field:
            auth_value = auth.get_request_auth_value()
            empty.update(
                {auth_field: auth_value}
            )

        # TODO conditional set based on actual doc_type
        doc_type = invoices_key

        dashboard = app.data.driver.db['dashboard_documents']

        # prepare bulk operation
        bulk = dashboard.initialize_ordered_bulk_op()

        # create empty DB if needed
        bulk.find(lookup).upsert().update(
            {
                '$setOnInsert': empty
            }
        )

        # increase stats as needed
        item = '%s.%d' % (doc_type, month)
        amount_item = '%s.%s' % (item, amount_key)
        quantity_item = '%s.%s' % (item, quantity_key)
        bulk.find(lookup).update(
            {
                '$inc': {amount_item: doc[total_key], quantity_item: 1}
            }
        )

        # execute bulk op
        r = bulk.execute()

        # TODO remove or switch to log?
        if app.config['DEBUG'] is True:
            from pprint import pprint
            pprint(r)
