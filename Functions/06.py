"""
Реализуйте функцию, которая получает в качестве аргумента
список чисел и преобразует его в список строк.
Используйте функциональное программирование.
"""


def stringify_list(num_list):
    return list(map(str, num_list))


n = int(input("Введите число: "))
print(stringify_list(range(n)))
