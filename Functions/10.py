"""
Напишите декоратор to_json, который можно применить к различным
функциям, чтобы преобразовывать их возвращаемое значение в JSON-формат.
"""

import functools
import json


def to_json(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return decorated


@to_json
def get_data():
    return {'data': 42}


print(get_data())  # вернёт '{"data": 42}'
