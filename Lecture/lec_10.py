import os
from pathlib import Path


######## Работа с каталогами

'''
✔ Определить текущий каталог
✔ Создать новый каталог
✔ Удалить существующий каталог
✔ Формирование пути
'''

file_1 = os.path.join(os.getcwd(), 'dir', 'new_file.txt')
print(f'{file_1 = }\n{file_1}')

file_2 = Path().cwd() / 'dir' / 'new_file.txt'
print(f'{file_1 = }\n{file_1}')
