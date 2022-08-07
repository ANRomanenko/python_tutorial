# Парсер файлов
('C:\\Users\\ARomanenko\\Desktop\\AutoRuns.11.70.Rus', ['AutoRuns.11.70.Rus'], [])


import os # Модуль по работе с операционной системой
import time # Модуль по работе со временем
spisok = []
for adress, dirs, files in os.walk('C:\\Users\ARomanenko\Desktop\AutoRuns.11.70.Rus'):
    for file in files:
        full = os.path.join(adress, file)
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)

print(spisok)