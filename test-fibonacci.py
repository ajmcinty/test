import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), [])

    def test_fibonacci_one(self):
        self.assertEqual(fibonacci(1), [0])

    def test_fibonacci_two(self):
        self.assertEqual(fibonacci(2), [0, 1])

    def test_fibonacci_five(self):
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])

    def test_fibonacci_ten(self):
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])

if __name__ == '__main__':
    unittest.main()