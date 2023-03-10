"""
В этот раз мы поменяем пользователя и компьютер из прошлой задачи местами.
Теперь пользователь в уме загадывает число между 1 и 100 (включительно).
Компьютер может спросить у пользователя: «Твое число больше, равно или меньше, чем число N?»,
где N — число, которое хочет проверить компьютер. Пользователь отвечает
одним из соответствующих вариантов: “больше”, “равно” или “меньше”.
"""

start, end = 1, 101
count = 0

while True:

    current = (start + end) // 2
    count += 1
    print("Твое число больше, равно или меньше, чем число {}? ".format(current))

    answer = input().lower()

    if not answer or answer == "exit":
        break

    if not(answer == "больше" or answer == "меньше" or answer == "равно"):
        print("Я вас не понимаю... Жду ответа 'больше', 'меньше' или 'равно'\n")

    if answer == "больше":
        start = current
    elif answer == "меньше":
        end = current
    elif answer == "равно":
        print("Число угадано! Число попыток:", count)
        break
