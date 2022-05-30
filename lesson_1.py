# Урок 1 - Переменные

number = 3
number = 4 # Теперь переменная number ссылается на 4
number2 = 5
result = number + number2
print('В переменной result находиться число:', result)

num1 = num2 = 5 # Мы присвоили двум переменным по числу 5
print(num1, num2)

# Множиственное присвоение
num_1, num_2 = 5, 7
print(num_1, num_2)

swap1 = 8
swap2 = 9
swap1, swap2 = swap2, swap1 + swap2
print(swap1, swap2)

swap2 -= number
print(swap2)

swap2 += 1
print(swap2)

print()

# Распаковка списка по периметру

*z, x, c = [1, 2, 3, 4 ,5]
print(z)
print(x)
print(c)

print()

for item in range(1, 25 + 1):
    print(item, end=' ')

print()

andr = 6
andr = 10
andr2 =15

res = andr + andr2 + 1
print(res)

res += 1
print(res)