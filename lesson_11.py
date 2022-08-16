# Словари, тип данных dict

d1 = {'a': 7, 'b': 10}
d2 = dict([[1, 2], [3, 4], [5, 6]])
d3 = dict().fromkeys([1, 2, 3, 4, 5], 'value')


# d5 = d1.copy()
# print(d1.items())
# print(d1.keys())
# print(d1.values())
# d1.update(d2)
# print(d1)


if 'c' in d1:
    print(d1['c'])

y = d1.get('c', 'value')
print(y)

t = d1.pop('a')
print(t, d1)


# price = {'meat': 3, 'bread': 1, 'potato': 0.5, 'water': 0.2}
#
# users = {
#     'Alex': {'password': 9856214, 'id': 1957},
#     'Jimmy99': {'password': 1236487, 'id': 9654},
#     'Bob33': {'password': 9546752, 'id': 6453}
# }


# def buy():
#     pay = 0
#     while True:
#         enter = input('Что покупаем???\n')
#         if enter == 'end':
#             break
#         pay += price[enter]
#     return pay

# print(d2)
# print(users['Alex']['password'])

# print(buy())
# print(d1)
# print(d1['a'])
# d1['b'] = 60
# print(d1)
# d1['a'] = 10
# print(d1)
# del d1['b']
# print(d1)
# print(d2)
# print(d3)