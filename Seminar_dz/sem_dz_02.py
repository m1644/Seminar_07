from File_utils import create_files, pseudonyms_name, file_operations


# Использование функции из пакета: (create_files.py)
extension_counts = {
    "txt": 1,
    "pdf": 1,
    "mp4": 1,
    "jpeg": 1,
    "png": 1
}

create_files.generate_files_with_extensions(extension_counts, min_name_length=4, max_name_length=8, min_file_size=256, max_file_size=4096)
# ------------------------ #


# Использование функции из пакета: (pseudonyms.py)
num_names = 8
pseudonyms = pseudonyms_name.generate_pseudonyms(num_names)
filename = "pseudonyms.txt"
pseudonyms_name.save_pseudonyms_to_file(pseudonyms, filename)
# ------------------------ #


# Использование функции из пакета: (file_operations.py)
directory = "Files_2"
final_name = "new"
num_digits = 2
source_extension = ".txt"
final_extension = ".doc"
name_range = (1, 4)

file_operations.rename_files(directory, final_name, num_digits, source_extension, final_extension, name_range)
# ------------------------ #
