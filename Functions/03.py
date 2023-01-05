"""
Создайте входной файл numbers.txt и запишите
туда N целых чисел, каждое в отдельной строке.
Напишите программу, которая выводит сумму этих
чисел в выходной файл answer.txt.
"""

with open('numbers.txt') as f_numbers, open('answer.txt', 'w') as f_answer:
    numbers_list = [int(i) for i in f_numbers]
    f_answer.write(str(sum(numbers_list)))
