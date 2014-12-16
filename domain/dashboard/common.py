from domain.common import required_integer, amount_key

# TODO consider removing the unique constraint on 'year' (for peformance)

year_key = 'y'
year = {
    'type': 'integer',
    'required': True,
    'unique': True,
}

quantity_key = 'q'
month_series = {
    'type': 'list',
    'maxlength': 12,
    'minlength': 12,
    'required': True,
    'schema': {
        'type': 'dict',
        'schema': {
            amount_key: required_integer,        # amount
            quantity_key: required_integer,      # quantity
        }
    }
}
