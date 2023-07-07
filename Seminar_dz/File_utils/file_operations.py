import os


'''
✔ Функция группового переименования файлов.
✔ Принимает параметр - желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
✔ Принимает параметр - количество цифр в порядковом номере.
✔ Принимает параметр - расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
✔ Принимает параметр - расширение конечного файла.
✔ Принимает диапазон - сохраняемого оригинального имени.
'''

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
