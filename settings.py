"""
    eve.settings
    ~~~~~~~~~~~~

    Default API settings. These can be overridden by editing this file or, more
    appropriately, by using a custom settings module (see the optional
    'settings' argument or the EVE_SETTING environment variable).

    :copyright: (c) 2012 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""
MONGO_HOST = 'ds035338.mongolab.com'
MONGO_PORT = 35338
MONGO_USERNAME = 'test'
MONGO_PASSWORD = 'test'
MONGO_DBNAME = 'heroku_app16785065'
SERVER_NAME = 'amica-test.herokuapp.com'

RESOURCE_METHODS = ['GET', 'POST']               # defauts to GET
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']       # defaults to GET

contacts = {
    'url': 'contatti',                      # defaults to resource key
    #'write_concern': {'w': 2},
    'extra_response_fields': ['token'],
    'cache_control': 'max-age=20,must-revalidate',
    'cache_expires': 20,
    'allowed_roles': ['admin'],
    'item_title': 'contatto',
    'additional_lookup': {
        'url': '[\w]+',   # to be unique field
        'field': 'name'
    },
    #'datasource': {'filter': {'username': {'$exists': False}}},
    'schema': {
        'active_list': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'p_id': {
                        'type': 'objectid',
                        'required': True,
                        'data_relation': {
                            'collection': 'users'
                        }
                    },
                    'proj_name': {
                        'type': 'string',
                    },
                    'perma_name': {
                        'type': 'string',
                    },
                    'raised': {
                        'type': 'integer',
                    },
                    'goal': {
                        'type': 'integer',
                    },
                    'description': {
                        'type': 'string',
                    }
                }
            }
        },
        'test': {
            'type': 'string',
            'default': 'i am a default value',
        },
        'name': {
            'type': 'string',
            'minlength': 2,
            #'maxlength': 5,
            'unique': True,
        },
        'role': {
            'type': 'list',
            'allowed': ["agent", "client", "vendor"],
        },
        'rows': {
            #'readonly': True,
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'sku': {'type': 'string'},
                    'price': {'type': 'integer', 'default': 10},
                },
            }
        },
        'alist': {
            #'readonly': True,
            'type': 'list',
            'items': [{'type': 'string'}, {'type': 'integer'}, ]
        },
        'location': {
            'type': 'dict',
            'schema': {
                'address': {'type': 'string'},
                'city': {'type': 'string', 'required': True}
            },
        },
        'born': {
            'type': 'datetime',
        },
        'cin': {
            'type': 'string',
            'cin': True,
        },
        'test': {
            'type': 'objectid',
            'data_relation': {
                'collection': 'invoices',
                'field': '_id'
            },
        }
    }
}


DOMAIN = {
    'contacts': contacts,
}
