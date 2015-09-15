# -*- coding: utf-8 -*-
"""
    adam.settings
    ~~~~~~~~~~~~~

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os
import adam.domain as domain

# Sensible settings are retrieved from environment variables when available in
# the hosting environment (Heroku), or set to default values for local testing.
if os.environ.get('TESTING') is None:
    MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
    MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
    MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'user')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'pw')
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'adam')
else:
    # Load MONGO settings from test suite.
    # Have to split into two lines in order to get the flake8 noqa tag in
    from tests import MONGO_DBNAME, MONGO_USERNAME, MONGO_PASSWORD  # noqa
    from tests import MONGO_HOST, MONGO_PORT # noqa

# $PORT is defined if we are hosted on Heroku
if os.environ.get('PORT') is None:
    DEBUG = True

# Allow full range of CRUD operations on resources and items
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'PUT']

# Enable 'User Restricted Resource Access' (see
# http://python-eve.org/authentication.html#user-restricted.) This will allow
# accounts to only edit/retrieve data created by themselves.
# AUTH_USERNAME_FIELD = domain.account_key

# Disable HATEOAS
HATEOAS = False

# Switch soft deletes on. Requires Eve 0.6+.
# See http://python-eve.org/features#soft-delete.
SOFT_DELETE = True

# We don't want pagination enabled.
PAGINATION = False

# We want the whole document back with POST/PATCH/PUT responses.
BANDWIDTH_SAVER = False

# Enable server information at the API homepage
INFO = '_info'

# Set the API domain
DOMAIN = domain.DOMAIN
