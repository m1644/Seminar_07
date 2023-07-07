import os
import random
import string


''' Задание_5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
'''

def generate_random_name(min_length=6, max_length=30):
    length = random.randint(min_length, max_length)
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_content(min_length=256, max_length=4096):
    length = random.randint(min_length, max_length)
    letters = string.ascii_letters + string.digits + string.punctuation + ' '
    return ''.join(random.choice(letters) for _ in range(length))

def create_files_with_extension(extension, min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096, num_files=42):
    folder_name = "files_1"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    for i in range(num_files):
        file_name = generate_random_name(min_name_length, max_name_length) + "." + extension
        file_size = random.randint(min_file_size, max_file_size)
        file_path = os.path.join(folder_name, file_name)
        
        content = generate_random_content()
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

def generate_files_with_extensions(extension_counts, min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096):
    for extension, num_files in extension_counts.items():
        create_files_with_extension(extension, min_name_length, max_name_length, min_file_size, max_file_size, num_files)

extension_counts = {
    "txt": 4,
    "pdf": 2,
    "csv": 4,
    "mp4": 2,
    "jpeg": 4,
    "png": 2
}

generate_files_with_extensions(extension_counts, min_name_length=6, max_name_length=30, min_file_size=256, max_file_size=4096)
