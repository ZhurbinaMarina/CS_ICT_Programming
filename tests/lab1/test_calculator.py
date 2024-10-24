import unittest
from src.lab1.calculator import Calculator


class CalculatorTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_one(self):
        self.assertEqual(1, 1)

    def test_addition(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1, 2), 3)

    def test_subtract(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(3, 2), 1)

    def test_multiply(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_divide(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(4, 2), 2)

    def test_division_by_zero(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(4, 0), "Cannot divide by zero.")

    def test_involution(self):
        calculator = Calculator()
        self.assertEqual(calculator.involution(2, 5), 32)
