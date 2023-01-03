"""
Напишите программу, которая считает количество специальных
символов в символьной строке. В рамках задачи к специальным
символам относятся символы из набора "@!#№$%&".
Набор должен храниться в виде множества.
"""

string = input("Введите строку: ")
character_set = {'@', '!', '#', '№', '$', '%', '&'}
string_list = list(string)
character_list = list(character_set)


def intersection(list1, list2):
    temp = set(list2)
    list3 = [value for value in list1 if value in temp]
    return list3


print("Количество специальных символов:", len(intersection(string_list, character_list)))
