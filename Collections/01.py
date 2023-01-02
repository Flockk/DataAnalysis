"""
Дано целое число N. Напишите программу,
которая формирует список из
нечётных чисел от 1 до N.
"""
number_list = []
number = int(input("Введите число: "))
for i in range(1, number, 2):
    number_list.append(i)
print(f'Список из нечётных чисел от 1 до {number}: ', number_list)