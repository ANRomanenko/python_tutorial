# Типы данных

a = None # Отсутствие данных - None
print(type(a))
a = 1 # Целое число - int
print(type(a))
a = 1.0 # Число с плавающей точкой - float
print(type(a))
a = 1 + 1j # Комплексное число - complex
print(type(a))
a = '1' # Строка - str
print(type(a))
a = [1, 1, 'a'] # Список - list
print(type(a))
a = (1, 1, 'a') # Кортеж - tuple
print(type(a))
a = {1, 2, 'a'} # Множества - set
print(type(a))
a = {'a': 1, 'b': 2} # Словарь - dict
print(type(a))
a = True # И логические булевые значения True или False - bool
print(type(a))

print(5 + 5.5)
print('string' + '12345')

print(5 + float('12345'))
print()

x = float(input('Введит первое число : '))
y = float(input('Введит второе число : '))
r = x + y
print('Получаем число: ' + str(r))