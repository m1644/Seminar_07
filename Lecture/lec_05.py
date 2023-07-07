

######## Менеджер контекста with open

with open('File/text_data.txt', 'r+', encoding='utf-8') as f:
    print(list(f))
# print(f.write('Пока'))  # ValueError: I/O operation on closed file.
# ------------------------
print('------------------------')


# Прошлые версии Python:

with open('File/text_data.txt', 'r+', encoding='utf-8') as f1, \
        open('File/bin_data.txt', 'rb') as f2, \
        open('File/data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3:
    print(list(f1))
    print(list(f2))
    print(list(f3))
# ------------------------
print('------------------------')


# Новые версии Python:

with (
        open('File/text_data.txt', 'r+', encoding='utf-8') as f1,
        open('File/bin_data.txt', 'rb') as f2,
        open('File/data.txt', 'r', encoding='utf-8', errors='backslashreplace') as f3
):
    print(list(f1))
    print(list(f2))
    print(list(f3))
