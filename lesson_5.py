# Цикл for Часть 1

name = 'Good Boy'
count = 0

for i in name:
    if i == 'o':
        print('В строке есть буква о')
        count += 1
    if i == 'd':
        break

else:
    print('Цикл завершен букв о:', count)

print('Программа продолжает работать дальше! \n')

# ---

name = 'Good Boy'
count = 0

for i in name:
    if i == 'o':
        continue
        print('В строке есть буква о')
        count += 1
    print(i)

else:
    print('Цикл завершен букв о найдено:', count)

print('Программа продолжает работать дальше! \n')