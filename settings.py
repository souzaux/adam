# -*- coding: utf-8 -*-
"""
    adam.settings
    ~~~~~~~~~~~~~

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os
import domain

# Sensible settings are retrieved from environment variables when available in
# the hosting environment (Heroku), or set to default values for local testing.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'test')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'test')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'adam-test')

# $PORT is defined if we are hosted on Heroku
if os.environ.get('PORT'):
    SERVER_NAME = 'amica-test.herokuapp.com'
else:
    # we're running on local
    SERVER_NAME = '127.0.0.1:5000'
    DEBUG = True

# Allow full range of CRUD operations on resources and items
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

# Enable 'User Restricted Resource Access' (see
# http://python-eve.org/authentication.html#user-restricted.) This will allow
# accounts to only edit/retrieve data created by themselves.
AUTH_USERNAME_FIELD = domain.account['key']

# Set the API domain
DOMAIN = domain.DOMAIN
