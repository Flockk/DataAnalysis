"""
Необходимо написать скрипт, который «нарисует» (выведет на консоль) лестницу.
Количество ступенек в лестнице передается скрипту в качестве параметра.
Гарантируется, что на вход подаются только целые числа > 0.
Чтение данных нужно произвести способом, аналогичным тому,
что описан в предыдущем задании. Ступени должны отображаться
с помощью символа решетки "#" и пробелов. Пример работы скрипта:
$ python solution.py 3
  #
 ##
###
"""

import sys

count = int(sys.argv[1])
for i in range(1, count + 1):
    print(' ' * (count - i) + '#' * i)
