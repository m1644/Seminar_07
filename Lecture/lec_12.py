import os
import shutil
from pathlib import Path


######## Работа с файлами

'''
✔ Переименование файлов
✔ Перемещение файлов
✔ Копирование файлов
✔ Удаление файлов
'''

'''
os.rename('old_name.py', 'new_name.py')

p = Path('old_file.py')
p.rename('new_file.py')

Path('new_file.py').rename('newest_file.py')
# ------------------------


os.replace('newest_file.py', os.path.join(os.getcwd(), 'dir', 'new_file.py'))

old_file = Path('new_name.py')
new_file = old_file.replace(Path.cwd() / 'new_os_dir' / old_file)
# ------------------------


shutil.copy('one.txt', 'dir')
shutil.copy2('two.txt', 'dir/one_more.txt')
# ------------------------
'''

# shutil.copytree('dir', 'one_more_dir')
# ------------------------

# shutil.rmtree('dir')
# ------------------------


os.remove('one_more_dir/one.txt')
Path('one_more_dir/one_more.txt').unlink()
