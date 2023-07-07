

######## Запись и добавление в файл

'''
res = f.write(text) - Запись методом write
f.writelines('\n'.join(text)) - Запись методом writelines
print(text, file=f) - print в файл
'''

# res = f.write(text) - Запись методом write

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
with open('File/new_data.txt', 'a', encoding='utf-8') as f:
    res = f.write(text)
    print(f'{res = }\n{len(text) = }')
# ------------------------
print('------------------------')


text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', ]
with open('File/new_data.txt', 'a', encoding='utf-8') as f:
    for line in text: 
        res = f.write(line)
        print(f'{res = }\n{len(line) = }')
# ------------------------
print('------------------------')


text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', ]
with open('File/new_data.txt', 'a', encoding='utf-8') as f:
    for line in text: 
        res = f.write(f'{line}\n')
        print(f'{res = }\n{len(line) = }')
# ------------------------
print('------------------------')


# f.writelines('\n'.join(text)) - Запись методом writelines

text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', ]
with open('File/new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))
# ------------------------
print('------------------------')


# print(text, file=f) - print в файл

text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', ]
with open('File/new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, file=f)
# ------------------------
print('------------------------')


text = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.', ]
with open('File/new_data.txt', 'a', encoding='utf-8') as f:
    for line in text:
        print(line, end='***\n##', file=f)
