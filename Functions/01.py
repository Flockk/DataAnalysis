"""
Реализуйте функцию, которая в качестве аргумента
получает строку и возвращает список слов этой строки.
"""

text = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. " \
       "Aenean commodo ligula eget dolor. Aenean massa. " \
       "Cum sociis natoque penatibus et"


def list_of_words(input_str):
    lst = input_str.split(' ')
    return lst


print(list_of_words(text))