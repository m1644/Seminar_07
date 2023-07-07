import random
import math


''' Задание_3
✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
✔ При достижении конца более короткого файла, возвращайтесь в его начало
'''

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return [line.strip() for line in lines]

def multiply_pairs(names_file, numbers_file, result_file):
    names = read_file(names_file)
    numbers = read_file(numbers_file)
    num_names = len(names)
    num_numbers = len(numbers)

    with open(result_file, 'w', encoding='utf-8') as file:
        for i in range(num_names):
            name = names[i]
            number_pair = numbers[i % num_numbers].split('|')
            first_num = int(number_pair[0])
            second_num = float(number_pair[1])
            result = first_num * second_num

            if result < 0:
                file.write(f"{name.lower().capitalize()} {-abs(result)}\n")
            else:
                file.write(f"{name.capitalize()} {result}\n")

names_file = "pseudonyms.txt"
numbers_file = "random_pairs.txt"
result_file = "result.txt"
multiply_pairs(names_file, numbers_file, result_file)
