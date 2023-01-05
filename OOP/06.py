"""
Пользователь вводит строку text. Напишите программу,
которая записывает введённую пользователем строку в новый файл.
Используйте операторы try except else finally. Обработайте возможные ошибки:
1. Попытка создания файла, который уже существует.
2. Проблема при открытии файла.
3. Неожиданная ошибка.
"""

text = input('Введите строку для записи в файл: ')
try:
    example_file = open('example.txt', 'x')

except FileExistsError:
    print('Файл example.txt уже существует!')

except FileNotFoundError or IsADirectoryError or PermissionError:
    print('Проблема при открытии файла!')

except:
    print("Неожиданная ошибка!")
else:
    example_file.write(text)
    example_file.close()
finally:
    print("Большое спасибо за ввод строки!")
