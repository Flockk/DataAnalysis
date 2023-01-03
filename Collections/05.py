"""
Создайте два списка, в каждом из которых лежит
10 случайных букв алфавита (могут повторяться).
Затем для каждого списка создайте словарь из пар
«индекс — значение» и выведите оба словаря на экран.
"""

from random import randint

first_list = []
second_list = []
count = 10

for i in range(count):
    first_list.append(chr(randint(1072, 1103)))
    second_list.append(chr(randint(1072, 1103)))

first_dict = {k: v for k, v in zip(range(10), first_list)}
second_dict = {k: v for k, v in zip(range(10), second_list)}

print("Первый список:", first_list,
      "\nВторой список:", second_list,
      "\nПервый словарь:", first_dict,
      "\nВторой словарь:", second_dict)
