def reshape(mapping, data):
    reshaped = {}
    for key, value in mapping.items():
        # if isinstance(value, str):
        if type(value) == str:
            keys = value.split('.')
            temp = data
            for k in keys:
                temp = temp.get(k, None)
                if temp is None:
                    break
            reshaped[key] = temp
        elif callable(value):
            reshaped[key] = value(data)
        # elif isinstance(value, dict):
        elif type(value) == dict:
            reshaped[key] = reshape(value, data)
    return reshaped


mapping = {
    'age': 'Age',
    'name': lambda obj: obj['FirstName'] + ' ' + obj['LastName'],
    'address': lambda obj: reshape(
        {
            'street': 'Address.Street',
            'coords': lambda obj: reshape(
                {
                    'lat': 'Address.Lat',
                    'lng': 'Address.Long',
                },
                obj
            ),
        },
        obj
    ),
}

data = {
    'Age': 25,
    'FirstName': 'Tom',
    'LastName': 'Bingus',
    'Address': {
        'Street': '1234 Dangus St',
        'Lat': 123,
        'Long': 10,
    },
}

print(reshape(mapping, data) == {'age': 25, 'name': 'Tom Bingus',
                                 'address': {'street': '1234 Dangus St', 'coords': {'lat': 123, 'lng': 10}}})
