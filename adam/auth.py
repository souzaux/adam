# -*- coding: utf-8 -*-
"""
    adam.auth.py
    ~~~~~~~~~~~~

    The auth class.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from flask import current_app as app
from eve.auth import TokenAuth
from domain.user_accounts import token_key, roles_key


class Auth(TokenAuth):
    """ This class implements Token Based Authentication for our API
    endpoints. Since the API itself is going to be on SSL, we're fine with this
    variation of Basic Authentication.

    For details on Eve authentication handling see:
    http://python-eve.org/authentication.html
    """
    def check_auth(self, token, allowed_roles, resource, method):
        accounts = app.data.driver.db['user_accounts']
        lookup = {token_key: token}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup[roles_key] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        if account:
            self.set_request_auth_value(account[app.config['ID_FIELD']])
        return account is not None
