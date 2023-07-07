import random
import string


'''
✔ Функция, которая генерирует псевдоимена.
✔ Полученные имена сохраняет в файл.
'''

def generate_pseudonyms(num_names):
    vowels = "aeiou"
    consonants = "".join(set(string.ascii_lowercase) - set(vowels))

    pseudonyms = []
    for _ in range(num_names):
        name_length = random.randint(4, 6)
        name = random.choice(string.ascii_uppercase)
        for _ in range(name_length - 1):
            if len(name) % 2 == 0:
                name += random.choice(consonants)
            else:
                name += random.choice(vowels)
        pseudonyms.append(name)
    return pseudonyms

def save_pseudonyms_to_file(pseudonyms, filename):
    with open(filename, 'w') as file:
        for pseudonym in pseudonyms:
            file.write(pseudonym + '\n')
