# -*- coding: utf-8 -*-
"""
    adam.tests.dashboard-documents.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test that the documents dashboard is properly initialized and updated
    as documents are added, edited and deleted.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""

import copy

from . import TestBase

from adam.domain import documents as docs
from adam.domain.common import company_key
from adam.domain import dashboard_documents as db
from adam.domain.dashboard.common import amount_key, quantity_key


class TestDashboardDocuments(TestBase):
    def setUp(self):
        super(TestDashboardDocuments, self).setUp()

        self.invoice = {
            docs.total_key: 1000,
            docs.date_key: "Tue, 16 Dec 2014 13:53:14 GMT",
            docs.type_key: docs.types.invoice,
            company_key: self.company_id
        }

        self.order = copy.copy(self.invoice)
        self.order[docs.type_key] = docs.types.customer_order
        self.order[docs.date_key] = "Wed, 05 Nov 2014 13:53:14 GMT"

    def _post_one_document(self, doc):
        doc, status = self.post(docs.url, doc)
        self.assert201(status)
        return doc

    def test_dashboard_documents_post(self):
        # dashboard is empty
        r, status = self.get(db.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 0)

        self._post_one_document(self.invoice)
        r, status = self.get(db.url)
        self.assert200(status)
        # one item in the dashboard now
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]

        # year is 2014
        self.assertEqual(item[db.year_key], 2014)
        # 12th item (Dec) of the invoices array has been initialized to 1000,1
        self.assertEqual(item[db.invoices_key][11][amount_key], 1000)
        self.assertEqual(item[db.invoices_key][11][quantity_key], 1)

        self._post_one_document(self.invoice)
        r, status = self.get(db.url)
        self.assert200(status)
        # dashboard has still 1 item
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]

        # but now we got 2 docs in December, for a total of 2k
        self.assertEqual(item[db.invoices_key][11][amount_key], 2000)
        self.assertEqual(item[db.invoices_key][11][quantity_key], 2)

        # post one order now
        self._post_one_document(self.order)

        r, status = self.get(db.url)
        self.assert200(status)

        # dashboard has still 1 item
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]

        # orders stats have been updated (Nov. month slot)
        self.assertEqual(item[db.orders_key][10][amount_key], 1000)
        self.assertEqual(item[db.orders_key][10][quantity_key], 1)
        # invoices stats are unchanged
        self.assertEqual(item[db.invoices_key][11][amount_key], 2000)
        self.assertEqual(item[db.invoices_key][11][quantity_key], 2)

    def test_dashboard_documents_put(self):
        id_key = self.app.config['ID_FIELD']
        etag_key = self.app.config['ETAG']

        # post an invoice. this will add a dashboard item
        # with stats for this single document (see the POST test)
        ret_doc = self._post_one_document(self.invoice)

        # lower the invoice amount
        doc = copy.copy(self.invoice)
        doc[docs.total_key] = 900

        id, etag = ret_doc[id_key], ret_doc[etag_key]
        # store the updated document
        ret_doc, status = self.put('%s/%s' % (docs.url, id), doc, etag)
        self.assert200(status)

        # grab new etag
        etag = ret_doc[self.app.config['ETAG']]

        # dashboard has one item
        r, status = self.get(db.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]

        # stats have been updated
        self.assertEqual(item[db.invoices_key][11][amount_key], 900)
        # while number of documents did not change
        self.assertEqual(item[db.invoices_key][11][quantity_key], 1)

        # increase invoice amount
        doc[docs.total_key] = 1100

        r, status = self.put('%s/%s' % (docs.url, id), doc, etag)
        self.assert200(status)

        # dashboard has still one item
        r, status = self.get(db.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]

        # stats have been updated
        self.assertEqual(item[db.invoices_key][11][amount_key], 1100)
        # number of documents did not change
        self.assertEqual(item[db.invoices_key][11][quantity_key], 1)

        # post an order now.
        ret_doc = self._post_one_document(self.order)

        # lower the order amount
        doc = copy.copy(self.order)
        doc[docs.total_key] = 900

        id, etag = ret_doc[id_key], ret_doc[etag_key]
        # store the updated document
        ret_doc, status = self.put('%s/%s' % (docs.url, id), doc, etag)
        self.assert200(status)

        # grab new etag
        etag = ret_doc[self.app.config['ETAG']]

        # dashboard has one item
        r, status = self.get(db.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]

        # order stats have been updated
        self.assertEqual(item[db.orders_key][10][amount_key], 900)
        # while number of documents did not change
        self.assertEqual(item[db.orders_key][10][quantity_key], 1)

        # increase invoice amount
        doc[docs.total_key] = 1100

        r, status = self.put('%s/%s' % (docs.url, id), doc, etag)
        self.assert200(status)

        # dashboard has still one item
        r, status = self.get(db.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]

        # order stats have been updated
        self.assertEqual(item[db.orders_key][10][amount_key], 1100)
        # number of documents did not change
        self.assertEqual(item[db.orders_key][10][quantity_key], 1)

    def test_dashboard_documents_delete(self):
        id_key = self.app.config['ID_FIELD']
        etag_key = self.app.config['ETAG']

        # post an invoice. this will add a dashboard item
        # with stats for this single document (see the POST test)
        ret_doc = self._post_one_document(self.invoice)

        id, etag = ret_doc[id_key], ret_doc[etag_key]
        # delete the document
        ret_doc, status = self.delete('%s/%s' % (docs.url, id), etag)
        self.assert204(status)

        # dashboard has one item
        r, status = self.get(db.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]

        # stats have been updated
        self.assertEqual(item[db.invoices_key][11][amount_key], 0)
        # while number of documents did not change
        self.assertEqual(item[db.invoices_key][11][quantity_key], 0)

        # post an order now.
        ret_doc = self._post_one_document(self.order)

        id, etag = ret_doc[id_key], ret_doc[etag_key]
        # delete the order
        ret_doc, status = self.delete('%s/%s' % (docs.url, id), etag)
        self.assert204(status)

        # dashboard has one item
        r, status = self.get(db.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]

        # stats have been updated
        self.assertEqual(item[db.invoices_key][11][amount_key], 0)
        # while number of documents did not change
        self.assertEqual(item[db.invoices_key][11][quantity_key], 0)
