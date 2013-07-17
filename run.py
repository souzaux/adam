# -*- coding: utf-8 -*-
"""
    adam.run.py
    ~~~~~~~~~~~

    The API launch script.

    :copyright: (c) 2013 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
from eve import Eve
from eve.auth import BasicAuth
import os


class Auth(BasicAuth):
    """ This class implements Basic Authentication for our API endpoints. Since
    the API itself is going to be on SSL, we're fine with BA. Also, in our use
    case, API clients will be mobile and web apps that we directly control so,
    for the time being, a single user/pw pair will do.

    The nice thing about having a custom proprietary class for auth handling
    is that we can always add complexity later, as the need arises, without
    touching the API configuration itself.

    For details on Eve authentication handling see:
    http://python-eve.org/authentication.html
    """
    def check_auth(self, username, password, allowed_roles, resource):
        if os.environ.get('PORT'):
            # We're hosted on heroku. Retrieve the valid user/pw pair from the
            # environment
            user = os.environ['AUTH_USERNAME']
            pw = os.environ['AUTH_PASSWORD']
        else:
            # We're running on a local environment, probably for testing
            # purposes. Allow for a trivial user/pw pair.
            user = 'username'
            pw = 'password'
        return username == user and password == pw


app = Eve(auth=Auth)

# Heroku defines a $PORT environment variable that we use to determine
# if we're running locally or not.
port = os.environ.get('PORT')
if port:
    host = '0.0.0.0'
    port = int(port)
else:
    host = None
    port = 5000

if __name__ == '__main__':
    app.run(host=host, port=port)
