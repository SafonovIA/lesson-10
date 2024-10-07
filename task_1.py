# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name():
    while True:
        word = ""
        for _ in range(2):
            for i in range(random.randint(1, 16)):
                word += chr(random.randint(97, 122))
            word += " "

        yield word

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))