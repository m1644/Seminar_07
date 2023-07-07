import os
from pathlib import Path


######## Чтение данных о каталогах

'''
✔ Получение списка каталогов и файлов
✔ Проверка на директорию, файл и ссылку
✔ Обход папок через os.walk()
'''

print(os.listdir())

p = Path(Path().cwd())
for obj in p.iterdir():
    print(obj)
# ------------------------
print('------------------------')


dir_list = os.listdir()
for obj in dir_list:
    print(f'{os.path.isdir(obj) = }', end='\t')
    print(f'{os.path.isfile(obj) = }', end='\t')
    print(f'{os.path.islink(obj) = }', end='\t')
    print(f'{obj = }')

p = Path(Path().cwd())
for obj in p.iterdir():
    print(f'{obj.is_dir() = }', end='\t')
    print(f'{obj.is_file() = }', end='\t')
    print(f'{obj.is_symlink() = }', end='\t')
    print(f'{obj = }')
# ------------------------
print('------------------------')


for dir_path, dir_name, file_name in os.walk(os.getcwd()):
    print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
