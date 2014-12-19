from collections import namedtuple
from adam.domain.common import required_integer, key as common_key

# TODO consider removing the unique constraint on 'year' (for peformance)
SchemaKey = namedtuple('SchemaKey', 'year, quantity, amount, company')
key = SchemaKey(
    year='y',
    quantity=common_key.quantity,
    amount=common_key.amount,
    company=common_key.company
)

year = {
    'type': 'integer',
    'required': True,
    'unique': True,
}

month_series = {
    'type': 'list',
    'maxlength': 12,
    'minlength': 12,
    'required': True,
    'schema': {
        'type': 'dict',
        'schema': {
            key.amount: required_integer,        # amount
            key.quantity: required_integer,      # quantity
        }
    }
}
