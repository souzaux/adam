# -*- coding: utf-8 -*-

"""
    Active tokens are stored in redis via the adam-auth. When a request hits
    a API endpoint all we need to do is verify that a token is provided with
    the request and that said token is active.

    adam-auth is a flask-sentinel instance which takes care of managing
    users and releasing tokens.

    :copyright: (c) 2015 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""
from eve.auth import BasicAuth
from eve.exceptions import ConfigException
from flask import request, current_app
from redis import StrictRedis


class BearerAuth(BasicAuth):
    """ Overrides Eve's built-in basic authorization scheme and uses Redis to
    validate bearer token
    """
    def __init__(self):
        super(BearerAuth, self).__init__()
        self.redis = StrictRedis()

    def check_auth(self, token, allowed_roles, resource, method):
        """ Check if API request is authorized.

        Examines token in header and checks Redis cache to see if token is
        valid. If so, request is allowed.

        :param token: OAuth 2.0 access token submitted.
        :param allowed_roles: Allowed user roles.
        :param resource: Resource being requested.
        :param method: HTTP method being executed (POST, GET, etc.)
        """
        if not token:
            return False

        user_id = self.redis.get(token)
        if not user_id:
            return False

        # now switching to the user-reserved mongo instance.

        mongo_prefix = 'MONGO%s' % user_id

        # TODO remove defaulting to localhost so exception is raised
        # if db host is not available. Right now, unless redis hodls a
        # key for the user, all dbs are hosted on localhost.
        host = self.redis.get(user_id) or 'localhost'
        if not host:
            raise ConfigException('Cannot locate host for user database %s' %
                                  user_id)

        uri = 'mongodb://%s/%s' % (host, user_id)

        current_app.config['%s_URI' % mongo_prefix] = uri

        self.set_mongo_prefix(mongo_prefix)

        return True

    def authorized(self, allowed_roles, resource, method):
        """ Validates the the current request is allowed to pass through.

        :param allowed_roles: allowed roles for the current request, can be a
                              string or a list of roles.
        :param resource: resource being requested.
        """
        try:
            token = request.headers.get('Authorization').split(' ')[1]
        except:
            token = None
        return self.check_auth(token, allowed_roles, resource, method)
