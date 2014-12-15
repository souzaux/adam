# -*- coding: utf-8 -*-
"""
    adam.dashboard.py
    ~~~~~~~~~~~~~~~~~

    Dashboard Module.

    This module updates the dashboard each time a sensible documents is
    added, updated or deleted.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""


import sys
from flask import current_app as app

this = sys.modules[__name__]


def dashboard_insert(resource, docs):
    """ Invokes the handling function for the resource involved. To append
    a new handler just name it '<resource_name>_insert'.
    """
    f = '%s_insert' % resource
    try:
        getattr(this, f)(docs)
    except AttributeError:
        pass


def dashboard_replace(resource, new, original):
    """ Invokes the handling function for the resource involved. To append
    a new handler just name it '<resource_name>_replace'.
    """
    f = '%s_replace' % resource
    try:
        getattr(this, f)(new, original)
    except AttributeError:
        pass


def dashboard_delete(resource, document):
    """ Invokes the handling function for the resource involved. To append
    a new handler just name it '<resource_name>_delete'.
    """
    f = '%s_delete' % resource
    try:
        getattr(this, f)(document)
    except AttributeError:
        pass


def documents_insert(docs):
    print app.data.driver
    for d in docs:
        print d
