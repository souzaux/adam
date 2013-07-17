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
        user = os.environ.get('AUTH_USERNAME', 'username')
        pw = os.environ.get('AUTH_PASSWORD', 'password')
        return username == user and password == pw


app = Eve(auth=Auth)

if __name__ == '__main__':
    # Heroku defines a $PORT environment variable, which we use to determine
    # if we're running locally or not.
    host = '0.0.0.0' if os.environ.get('PORT') else None
    app.run(host=host, port=int(os.environ.get('PORT', 5000)))
