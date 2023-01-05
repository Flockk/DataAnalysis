"""
Реализуйте класс-итератор Primes, который принимает максимальное
число N и выдаёт все простые числа от 1 до N.
"""


class Primes:
    """Итератор для определения простых чисел"""

    def __init__(self, end):
        self.end = end
        self.current = 0
        self.prime_numbers = []

    def __iter__(self):
        """Получаем итератор для перебора чисел"""
        self.current = 1
        return self

    def is_prime(self):
        """Проверка числа на простоту"""
        self.current += 1
        for prime in self.prime_numbers:
            if self.current % prime == 0:
                return None
        self.prime_numbers.append(self.current)
        return self.current

    def __next__(self):
        """Переход к следующему числу"""
        value = None
        while value is None:
            value = self.is_prime()
        if self.current < self.end:
            return value
        else:
            raise StopIteration()


if __name__ == '__main__':
    prime_nums = Primes(50)
    for i_elem in prime_nums:
        print(i_elem, end=' ')
