"""
На вход в программу подаётся url-адрес в виде строки.
Напишите программу, которая проверяет вхождение подстроки “documentlibrary”,
а также проверяет, что url начинается на “https”.
Выведите соответствующие сообщения.
"""

url = input("Введите url: ")

if not (url.startswith("https")):
    print("Ошибка: адрес не начинается с https.")
elif not ("documentlibrary" in url):
    print("Ошибка: подстрока documentlibrary не обнаружена.")
else:
    print("Адрес указан верно.")
