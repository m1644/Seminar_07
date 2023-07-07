import shutil
import os
from pathlib import Path


######## Файловая система

print(os.getcwd())
print(Path.cwd())
os.chdir('../..')
print(os.getcwd())
print(Path.cwd())
# ------------------------


os.mkdir('new_os_dir')
Path('new_path_dir').mkdir()
# ------------------------


os.makedirs('dir/other_dir/new_os_dir')
# Path('some_dir/dir/new_path_dir').mkdir()  # FileNotFoundError: [WinError 3] Системе не удается найти указанный путь: 'some_dir\\dir\\new_path_dir'
Path('some_dir/dir/new_path_dir').mkdir(parents=True)
# ------------------------


# os.rmdir('dir')  # OSError: [WinError 145] Папка не пуста: 'dir'
# Path('some_dirr').rmdir()  # OSError: [WinError 145] Папка не пуста: 'some_dirr'
os.rmdir('dir/other_dir/new_os_dir')
Path('some_dir/dir/new_path_dir').rmdir()


shutil.rmtree('dir/other_dir')
shutil.rmtree('some_dir')
