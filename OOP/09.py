"""
В классе TestFactorization, потомке TestCase, создан метод test_simple_multipliers().
Требуется написать проверку того, что a умножить на b равно x,
с использованием унаследованного от TestCase метода assertEqual.
"""

import unittest


class TestFactorization(unittest.TestCase):
    def test_simple_multipliers(self):
        x = 77
        a, b = factorize(x)
        self.assertEqual(a * b, x)


def factorize(x):
    a = x / 20
    b = 20
    return a, b


if __name__ == "__main__":
    unittest.main()
