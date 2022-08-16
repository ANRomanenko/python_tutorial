# Словари dict()
# Часть 2. Итерия

price = {'meat': 2, 'bread': 1, 'potato': 0.5, 'water': 0.2}

for value in price.values():
    print(value)

print()

for keys in price.keys():
    print(keys)


# new = {}
# for key, value in price.items():
#     new[value] = key
# print(new)
#
# x = price.values()
# print(x)
# print(list(x))

# new_price = {}
#
# for i in price:
#     new_price[i] = round(price[i] * 0.85, 2)

# print(price)
# print(new_price)

# x = price.items()
# print(x)