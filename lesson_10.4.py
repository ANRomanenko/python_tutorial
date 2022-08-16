def calc():
    a = float(input('Введите первое число: '))
    return a


def calc_1():
    b = float(input('Введите второе число: '))
    return b


def result():
    a = calc()
    b = calc_1()
    c = a + b
    return c


print('Сумма результата: ', result(), f'Мы ввели первое число: {print(calc())}', f'Мы ввели второе число: {calc_1()}')
