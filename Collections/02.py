"""
Дан список из N чисел. Напишите программу,
которая сортирует элементы списка по возрастанию
и выводит его на экран. Решите задачу двумя способами:
первый - с использованием встроенной функции для сортировки;
второй - без использования этой функции. Во втором случае
постарайтесь написать как можно более эффективный алгоритм сортировки.
"""
from random import randint

number_list = []
number = int(input("Введите число: "))
for i in range(number):
    number_list.append(randint(-100, 100))
print("Изначальный список:", number_list)
print(f"Отсортированный список (встроенная функция): {sorted(number_list)}")


def quick_sort(_list):
    length = len(_list)
    if length <= 1:
        return _list
    else:
        middle = _list.pop()

    elements_upper = []
    elements_lower = []

    for element in _list:
        if element > middle:
            elements_upper.append(element)
        else:
            elements_lower.append(element)

    return quick_sort(elements_lower) + [middle] + quick_sort(elements_upper)


print(f"Отсортированный список (быстрая сортировка): {quick_sort(number_list)}")
