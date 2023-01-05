"""
В файле numbers.txt есть N чисел, разделённых пробелами.
Напишите программу, которая подсчитает общую сумму чисел в
файле. Для считывания файла реализуйте специальный генератор.
"""

import random as rand

with open('numbers.txt', 'w') as fw_numbers:
    numbers_list = (rand.randint(1, 100) for i in range(1_000_000))  # 1 000 000 случайных чисел
    fw_numbers.write(' '.join(map(str, numbers_list)))

with open('numbers.txt', 'r') as fr_numbers:
    r = fr_numbers.read()
    sum_numbers = sum(int(x) for x in r.split())
    print("Сумма чисел в файле: {}".format(sum_numbers))
