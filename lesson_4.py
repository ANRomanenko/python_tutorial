# Цикл while
# Цикл while исполняет блок кода до тех пор пока условие верно

x = 0 # В программирование есть такое понятие как переменная счётчик

while x < 5:
    x += 1
    print(x)

else: # У цикла есть необязательный оператор else
    print()
    print('Программа завершена!')

print()


# while True: # Получаем вычисление фактариала
#     x = int(input('Ввод: '))
#     count = 0
#     y = 1
#
#     while count < x:
#         count += 1
#         y *= count
#
#     else:
#         print(y)

x = ''

while len(x) < 5:
    y = input('Ввод данных: ')
    if y == 'o':
        continue
    if y == 'l':
        break

    x += y

else:
    print(x)

print('Программа работает дальше!')