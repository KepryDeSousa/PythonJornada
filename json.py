import json

d1 = {
    'pessoa 1': {
        'nome':'jose',
        'idade':'122',
    },
    'pessoa 2':{
        'nome':'joao',
        'idade':'30',
    },
}
d1json = json.dumps(d1)
print(d1json)