"""
Пользователь вводит число N. Выведите пятую степень
каждого нечётного числа в диапазоне от единицы до N включительно.
Для этого используйте шаг внутри функции range.
"""

n = int(input('Введите число n: '))
for number in range(1, n + 1, 2):
    print(number, "** 5 =", number ** 5)