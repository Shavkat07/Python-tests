# def header(func):
#
#     def inner(*args, **kwargs):
#         print('<h1>')
#         func(*args, **kwargs)
#         print('</h1>')
#
#     return inner

from functools import wraps


def table(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


# @header  # say = header(table(say))
@table  # say = table(say)
def say(name, surname, age):
    print('hello world', name, surname, age)


def sqr(x):
    """
    Функция возводит число в квадрат
    :param x:
    :return:
    """
    print(x ** 2)


# say = header(table(say))

say('Vasya', 'Ivanov', '544')
