# Списки - list Часть 1
# Списки, тип данных list

m = [1, 2, 1, 3, 5, 'a', [5, 7, 10], ['s', 'f']]
print(m[-1][0])

# ---

s = [[5, 6], [1, 3], ['s', 'f']]

s[0] = 9

print(s)

s[0] = s[0] + 2

print(s)
print()
# ---

# Меняем списки местами!

y = [[5, 6], [1, 3], ['s', 'f']]

y[1], y[2] = y[2], y[1]

print(y)
print()

# К списку прибаляем значение с другого списка!

x = [[5, 6], [1, 3], ['s', 'f']]

x = x + [7] # Прибавляем значение другого списка в наш список
x = x * 2 # Умножаем наши списки
print(x)
print()

# --
name = list(range(10))
m = []
for i in name:
    if i == 8:
        continue
    if i == 5:
        continue
    m += [i]

else:
    print(m)

lis = [[1, 3, 5], ['spisok', 'name']]

lis = lis + [7]

lis[1], lis[2] = lis[2], lis[1]

print(lis)