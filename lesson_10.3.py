# Функция и структура кода, передача значений между Функциями

import math

PI = math.pi


def radius():
    n = float(input('Введите диаметер цилиндра в см: '))
    n /= 2
    return n


def height():
    m = float(input('Введите высоту цилиндра в см: '))
    return m


def volume():
    r = radius()
    h = height()
    s = PI * r ** 2
    v = s * h
    return v


# print('Объём цилиндра', volume(), 'см3')

def massa(g):
    n = float(input('Удельный вес г/см3: '))
    return g * n / 1000


print('Вес цилиндра в кг:', massa(volume()))

