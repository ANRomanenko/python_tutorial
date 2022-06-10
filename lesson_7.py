# Тип данных Кортеж (tuple)
# Кортеж это не изменяемый тип данных
# Кортежи быстрее итерируються циклами
# Меньше занимают места в памяти
# И самое главное это не изменяемый тип данных

x = (9, 8, 7, 6, 9, 5, 4, 9, 3)
print(x.count(9))
print(x.index(9))

h = (1, 2, 3)
g = h
h += (4, 5)
print(h)
print(g)




# y = []
# for i in range(len(x)):
#     y.append(x[i] + 3)
#
# print(y)
# print(x)
#
# t = list(x)
# t[0] = 10
#
# x = tuple(t)
# print(x)
#
# print(x[1:5])

#--

# print(x[0] + 5)
# print(x)
#
# # z, c, b = x
#
# r = 5
# u = 7
#
# r, u = u, r
#
# print(x[1:5])
#
# # print()
# # print(z)
# # print(c)
# # print(b)