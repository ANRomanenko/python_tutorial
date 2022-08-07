# Переменное количество аргументов def (*args) (название звёздочки "*" - астериск)

# def name(h, g, *args, key):
#     print(h)
#     print(g)
#     print(args)
#     print(key)
#
#
# name(1, 2, 3, 5, 6, key=10)

def exlusive_item(*args, key=False):
    new_list = []
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    if key == True:
        new_list.sort()
    return new_list


z = [9, 8, 7]
x = [8, 8, 9, 6, 7, 5]
c = [1, 2, 3, 4, 5, 6, 7, 7]

t = exlusive_item(z, x, c, key=True)
print(t)