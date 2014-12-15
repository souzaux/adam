# -*- coding: utf-8 -*-
"""
    adam.run.py
    ~~~~~~~~~~~

    The API launch script.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os
from eve import Eve
from eve.auth import TokenAuth
from dashboard import dashboard_insert, dashboard_delete, dashboard_replace


class Auth(TokenAuth):
    """ This class implements Token Based Authentication for our API
    endpoints. Since the API itself is going to be on SSL, we're fine with this
    variation of Basic Authentication.

    For details on Eve authentication handling see:
    http://python-eve.org/authentication.html
    """
    def check_auth(self, token, allowed_roles, resource, method):
        accounts = app.data.driver.db['accounts']
        lookup = {'t': token}
        if allowed_roles:
            # only retrieve a user if his roles match ``allowed_roles``
            lookup['r'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        if account:
            self.set_request_auth_value(account['_id'])
        return account is not None

app = Eve(auth=Auth)

app.on_inserted += dashboard_insert
app.on_replaced += dashboard_replace
app.on_deleted_item += dashboard_delete

# Heroku defines a $PORT environment variable that we use to determine
# if we're running locally or not.
port = os.environ.get('PORT')
if port:
    host = '0.0.0.0'
    port = int(port)
else:
    host = '127.0.0.1'
    port = 5000

if __name__ == '__main__':
    app.run(host=host, port=port)
