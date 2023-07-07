

######## Чтение файла

'''
list(f) - Чтение в список
res = f.read() - Чтение методом read
res = f.readline() - Чтение методом readline
for line in f: - Чтение циклом for
'''

# list(f) - Чтение в список

with open('File/text_data.txt', 'r', encoding='utf-8') as f:
    print(list(f))
# ------------------------
print('------------------------')


# res = f.read() - Чтение методом read

with open('File/text_data.txt', 'r', encoding='utf-8') as f:
    res = f.read()
    print(f'Читаем первый раз\n{res}')
    res = f.read()
    print(f'Читаем второй раз\n{res}')
# ------------------------
print('------------------------')


SIZE = 50
with open('File/text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.read(SIZE):
        print(res)
# ------------------------
print('------------------------')


# res = f.readline() - Чтение методом readline

with open('File/text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline():
        print(res)
# ------------------------
print('------------------------')


SIZE = 50
with open('File/text_data.txt', 'r', encoding='utf-8') as f:
    while res := f.readline(SIZE):
        print(res)
# ------------------------
print('------------------------')


# for line in f: - Чтение циклом for

with open('File/text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
# ------------------------
print('------------------------')


with open('File/text_data.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line[:1])
        print(line.replace('\n', ''))
