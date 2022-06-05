# Цикл for Часть 2

x = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'
y = input('Введите строку: \n')


for i in x:
    count = 0
    for r in y:
        if i == r:
            count += 1
    if count > 0:
        print('Букв', i, 'было', count)

# ---

for x in range(3 + 1):
    print(x)