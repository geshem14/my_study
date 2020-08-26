# week 2 task 2
# https://www.coursera.org/learn/diving-in-python/programming/0664k/
# diekorator-to-json
"""
Чтобы передавать данные между функциями, модулями или разными системами
используются форматы данных. Одним из самых популярных форматов является JSON.
Напишите декоратор to_json, который можно применить к различным функциям,
чтобы преобразовывать их возвращаемое значение в JSON-формат. Не забудьте
про сохранение корректного имени декорируемой функции.
"""
import functools
import json


def to_json(func):
    @functools.wraps(func)
    # if type(parm) == ???
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return wrapped


@to_json
def get_data(d_parm):
    return {'data': d_parm}


# temp = get_data(0)
# print(temp)

# temp = get_data([0, 0, 0])
# print(temp)

# temp = get_data({'0': 'v0'})
# print(temp)

