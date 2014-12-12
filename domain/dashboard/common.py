from domain.common import required_integer

month_series = {
    'type': 'list',
    'maxlength': 12,
    'minlength': 12,
    'required': True,
    'schema': {
        'type': 'dict',
        'schema': {
            'a': required_integer,      # amount
            'q': required_integer,      # quantity
        }
    }
}
