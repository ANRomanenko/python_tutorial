# Фунеции, область видимости переменных

x = 5


def name():
    x = 10

    def name2():
        nonlocal x
        x = 100
        print(x)

    name2()
    print(x)


name()
print(x)




# x = 5
#
#
# def name():
#
#     x = 100
#
#     return name2(x)
#
#
# def name2(par):
#     print(par)
#
#
# name()