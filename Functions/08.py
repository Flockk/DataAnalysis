"""
У нас есть функция, которая принимает список чисел и
возвращает сумму этих чисел. Реализуйте два декоратора:
1. Декоратор, который записывает в файл log.txt
результат декорируемой функции.
2. Декоратор с параметром, который записывает
результат в указанный файл.
"""

import functools


def first_logger(func):
    @functools.wraps(func)
    def decorated(num_list):
        result = func(num_list)
        with open('log.txt', 'w') as f_log:
            f_log.write(str(result))
        return result

    return decorated


def second_logger(filename):
    def decorator(func):
        def decorated(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as f_new_log:
                f_new_log.write(str(result))
            return result

        return decorated

    return decorator


@first_logger
def first_summator(nums_list):
    return sum(nums_list)


@second_logger('new_log.txt')
def second_summator(nums_list):
    return sum(nums_list)


with open('log.txt', 'r') as f, open('new_log.txt', 'r') as file:
    print('Результат первого декоратора: {}'.format(first_summator([1, 2, 3, 4, 5])),
          '\nlog.txt: {}'.format(f.read()),
          '\nРезультат второго декоратора: {}'.format(second_summator([1, 2, 3, 4, 5, 6])),
          '\nnew_log.txt: {}'.format(file.read()))
