"""
Напишите программу, которая генерирует случайное целое число
в диапазоне от 1 до 10 и запрашивает у пользователя число
до тех пор, пока он его не отгадает.
"""

import random

number = random.randint(1, 10)
count = 0

while True:

    count += 1
    answer = input("Введите число: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Введите правильное число!")
        continue

    user_answer = int(answer)

    if user_answer > number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif user_answer < number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Вы угадали! Число попыток:", count)
        break
      
