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
from adam.domain import dashboard_documents as dbdocs
from adam.domain.dashboard.common import key as month


class TestDashboardDocuments(TestBase):
    def setUp(self):
        super(TestDashboardDocuments, self).setUp()

        self.invoice = {
            docs.key.total: 1000,
            docs.key.date: "Tue, 16 Dec 2014 13:53:14 GMT",
            docs.key.type: docs.doctype.invoice,
            docs.key.company: self.company_id
        }

        self.order = copy.copy(self.invoice)
        self.order[docs.key.type] = docs.doctype.customer_order
        self.order[docs.key.date] = "Wed, 05 Nov 2014 13:53:14 GMT"

    def _post_one_document(self, doc):
        doc, status = self.post(docs.url, doc)
        self.assert201(status)
        return doc

    def test_dashboard_documents_post(self):
        # dashboard is empty
        r, status = self.get(dbdocs.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 0)

        self._post_one_document(self.invoice)
        r, status = self.get(dbdocs.url)
        self.assert200(status)
        # one item in the dashboard now
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        dec = item[dbdocs.key.invoices][11]

        # year is 2014
        self.assertEqual(item[dbdocs.key.year], 2014)
        # 12th item (Dec) of the invoices array has been initialized to 1000,1
        self.assertEqual(dec[month.amount], 1000)
        self.assertEqual(dec[month.quantity], 1)

        self._post_one_document(self.invoice)
        r, status = self.get(dbdocs.url)
        self.assert200(status)
        # dashboard has still 1 item
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        dec = item[dbdocs.key.invoices][11]

        # but now we got 2 docs in dec, for a total of 2k
        self.assertEqual(dec[month.amount], 2000)
        self.assertEqual(dec[month.quantity], 2)

        # post one order now
        self._post_one_document(self.order)

        r, status = self.get(dbdocs.url)
        self.assert200(status)

        # dashboard has still 1 item
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        dec = item[dbdocs.key.invoices][11]
        nov = item[dbdocs.key.orders][10]

        # orders stats have been updated (Nov. month slot)
        self.assertEqual(nov[month.amount], 1000)
        self.assertEqual(nov[month.quantity], 1)
        # invoices stats are unchanged
        self.assertEqual(dec[month.amount], 2000)
        self.assertEqual(dec[month.quantity], 2)

    def test_dashboard_documents_put(self):
        id_key = self.app.config['ID_FIELD']
        etag_key = self.app.config['ETAG']

        # post an invoice. this will add a dashboard item
        # with stats for this single document (see the POST test)
        ret_doc = self._post_one_document(self.invoice)

        # lower the invoice amount
        doc = copy.copy(self.invoice)
        doc[docs.key.total] = 900

        id, etag = ret_doc[id_key], ret_doc[etag_key]
        # store the updated document
        ret_doc, status = self.put('%s/%s' % (docs.url, id), doc, etag)
        self.assert200(status)

        # grab new etag
        etag = ret_doc[self.app.config['ETAG']]

        # dashboard has one item
        r, status = self.get(dbdocs.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        dec = item[dbdocs.key.invoices][11]

        # stats have been updated
        self.assertEqual(dec[month.amount], 900)
        # while number of documents did not change
        self.assertEqual(dec[month.quantity], 1)

        # increase invoice amount
        doc[docs.key.total] = 1100

        r, status = self.put('%s/%s' % (docs.url, id), doc, etag)
        self.assert200(status)

        # dashboard has still one item
        r, status = self.get(dbdocs.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        dec = item[dbdocs.key.invoices][11]

        # stats have been updated
        self.assertEqual(dec[month.amount], 1100)
        # number of documents did not change
        self.assertEqual(dec[month.quantity], 1)

        # post an order now.
        ret_doc = self._post_one_document(self.order)

        # lower the order amount
        doc = copy.copy(self.order)
        doc[docs.key.total] = 900

        id, etag = ret_doc[id_key], ret_doc[etag_key]
        # store the updated document
        ret_doc, status = self.put('%s/%s' % (docs.url, id), doc, etag)
        self.assert200(status)

        # grab new etag
        etag = ret_doc[self.app.config['ETAG']]

        # dashboard has one item
        r, status = self.get(dbdocs.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        nov = item[dbdocs.key.orders][10]

        # order stats have been updated
        self.assertEqual(nov[month.amount], 900)
        # while number of documents did not change
        self.assertEqual(nov[month.quantity], 1)

        # increase invoice amount
        doc[docs.key.total] = 1100

        r, status = self.put('%s/%s' % (docs.url, id), doc, etag)
        self.assert200(status)

        # dashboard has still one item
        r, status = self.get(dbdocs.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        nov = item[dbdocs.key.orders][10]

        # order stats have been updated
        self.assertEqual(nov[month.amount], 1100)
        # number of documents did not change
        self.assertEqual(nov[month.quantity], 1)

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
        r, status = self.get(dbdocs.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        dec = item[dbdocs.key.invoices][11]

        # stats have been updated
        self.assertEqual(dec[month.amount], 0)
        # while number of documents did not change
        self.assertEqual(dec[month.quantity], 0)

        # post an order now.
        ret_doc = self._post_one_document(self.order)

        id, etag = ret_doc[id_key], ret_doc[etag_key]
        # delete the order
        ret_doc, status = self.delete('%s/%s' % (docs.url, id), etag)
        self.assert204(status)

        # dashboard has one item
        r, status = self.get(dbdocs.url)
        self.assert200(status)
        self.assertEqual(len(r['_items']), 1)

        item = r['_items'][0]
        dec = item[dbdocs.key.invoices][11]

        # stats have been updated
        self.assertEqual(dec[month.amount], 0)
        # while number of documents did not change
        self.assertEqual(dec[month.quantity], 0)
