import os


''' Задание_1
✔ Напишите функцию группового переименования файлов. Она должна:
✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 
из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
'''

# Предусловие: в директории "files" находятся 2 файла (file_1.txt и file_2.txt).

def rename_files(directory, final_name, num_digits, source_extension, final_extension, name_range=None):
    files = os.listdir(directory)
    count = 1
    for file in files:
        if file.endswith(source_extension):
            file_path = os.path.join(directory, file)
            file_name, file_ext = os.path.splitext(file)
            if name_range is not None:
                start_index, end_index = name_range
                original_name = file_name[start_index - 1:end_index]
            else:
                original_name = file_name

            new_name = f"{original_name}_{final_name}_{str(count).zfill(num_digits)}{final_extension}"
            new_path = os.path.join(directory, new_name)

            os.rename(file_path, new_path)
            count += 1

directory = "Files_1"
final_name = "new"
num_digits = 2
source_extension = ".txt"
final_extension = ".docx"
name_range = (1, 4)

rename_files(directory, final_name, num_digits, source_extension, final_extension, name_range)
