import random


''' Задание_1
✔ Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
✔ Первое число int, второе - float разделены вертикальной чертой.
✔ Минимальное число - -1000, максимальное - +1000.
✔ Количество строк и имя файла передаются как аргументы функции. 
'''

def write_random_pairs(filename, num_lines):
    with open(filename, 'a') as file:
        for _ in range(num_lines):
            first_num = random.randint(-1000, 1000)
            second_num = random.uniform(-1000, 1000)
            line = f"{first_num}|{second_num}\n"
            file.write(line)

filename = "random_pairs.txt"
num_lines = 10
write_random_pairs(filename, num_lines)
