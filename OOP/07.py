"""
Дан файл names.txt, в котором построчно хранится N имён пользователей.
Напишите программу, которая берёт количество символов в каждой строке
файла и в качестве ответа выводит общую сумму в консоль. Если в какой-либо
строке меньше пяти символов, то вызывается ошибка, и программа завершается.
"""


class LengthError(BaseException):
    """Сообщение об ошибке при неправильной длине"""

    def __init__(self, message):
        self.message = message


def main():
    with open('names.txt', 'r', encoding='utf-8') as f_names:
        name_str = f_names.read().split('\n')
        print(name_str)
        result = ''.join(name_str)
        try:
            for count, name in enumerate(name_str):
                if len(name) < 3:
                    raise LengthError(f'Менее трёх символов в строке!')
        except LengthError:
            print(f'Менее трёх символов в строке!')
        else:
            print(f'Общее количество символов: {len(result)}')


if __name__ == '__main__':
    main()
