# Функции часть № 2 Параметры

def count_list(param, par2=False, count=0): # Параметер, это переменная определённая только внутри функции
    if par2 == True:
        typ = type(param[0])
        for i in param:
            count += 1
        return count, typ
    else:
        for i in param:
            count += 1
        return count


j = [9, 8, 7, 6]

h, p = count_list(j, True) # Аргумент
print(h)
print(p)


a = ['dron', 'andron', 'drons']


def dlina(par):
    count = 0
    for i in par:
        count += 1
    return count


y = dlina(a)
print(y)
