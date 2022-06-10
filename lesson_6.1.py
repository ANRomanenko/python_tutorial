# Списки - list Часть 2
# Списки, тип данных list

n = list(range(1, 20 + 1))
b = n.copy()
m = []


for i in n:
    if i % 2 == 0:
        m.append(i)
        n.remove(i)

else:
    print(n)
    print(m)
    print(b)

print(6 % 2)

# x = [9, 8, 7, 6, 5]
# x.append(4)
# x.insert(1, 7)
# print(x.count(7))
# x.sort()
# x.reverse()
# y = x.pop(0)
# print(y)
# x.remove(7)
# x.clear()
# x.extend(['a', 's'])
# h = x.copy()
#
# print(h, x)