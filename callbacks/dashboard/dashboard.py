# -*- coding: utf-8 -*-
"""
    adam.callbacks.dashboard.dashboard.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Dashboard callbacks dispatcher.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from callbacks.dashboard.documents import documents_insert, document_replace, \
    document_delete


def init(app):
    app.on_inserted_documents += documents_insert
    app.on_replaced_documents += document_replace
    app.on_deleted_item_documents += document_delete
