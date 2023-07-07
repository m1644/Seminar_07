

######## Методы перемещения в файле

'''
f.tell() - Метод tell возвращает текущую позицию в файле.
seek(offset, whence=0) - offset — смещение относительно опорной точки, whence — способ выбора опороной точки.
truncate(size=None) - Метод изменяет размер файла.
Если не передать значение в параметр size будет удалена часть файла от текущей позиции до конца.
'''


# f.tell()

text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', ]
with open('File/new_data_2.txt', 'a', encoding='utf-8') as f:
    print(f.tell())
    for line in text:
        f.write(f'{line}\n')
        print(f.tell())
    print(f.tell())
# print(f.tell())  # ValueError: I/O operation on closed file.
# ------------------------
print('------------------------')


# seek(offset, whence=0)

last = before = 0
text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', ]
with open('File/new_data_2.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
        print(f'{last = }, {before = }')
    print(f'{last = }, {before = }')
    print(f'{f.seek(before, 0) = }')
    f.write('\n'.join(text))
# ------------------------
print('------------------------')


# truncate(size=None)

last = before = 0
with open('File/new_data_2.txt', 'r+', encoding='utf-8') as f:
    while line := f.readline():
        last, before = f.tell(), last
    print(f'{f.seek(before, 0) = }')
    print(f.truncate())
# ------------------------
print('------------------------')


SIZE = 44
with open('File/new_data_2.txt', 'r+', encoding='utf-8') as f:
    print(f.truncate(SIZE))
