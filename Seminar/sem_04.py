import os
import random
import string


''' Задание_4
✔ Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры:
✔ расширение
✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
✔ количество файлов, по умолчанию 42
✔ Имя файла и его размер должны быть в рамках переданного диапазона.
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
    folder_name = "files"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    for i in range(num_files):
        file_name = generate_random_name(min_name_length, max_name_length) + "." + extension
        file_size = random.randint(min_file_size, max_file_size)
        file_path = os.path.join(folder_name, file_name)
        
        content = generate_random_content()
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

extension = "txt"
min_name_length = 6
max_name_length = 30
min_file_size = 256
max_file_size = 4096
num_files = 42

create_files_with_extension(extension, min_name_length, max_name_length, min_file_size, max_file_size, num_files)
