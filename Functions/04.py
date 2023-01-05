"""
Напишите программу, которая выводит на экран
абсолютный и относительный пути до файла
numbers.txt, созданный в предыдущей задаче.
"""
import os

print("Абсолютный путь:", os.path.abspath('numbers.txt'),
      "\nОтносительный путь:", os.path.join('PycharmProjects', 'pythonProject', 'numbers.txt'))
