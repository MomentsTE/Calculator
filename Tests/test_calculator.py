import unittest
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.calculate(2, 3, "+")
        self.assertEqual(result, 5)

    def test_subtraction(self):
        result = self.calculator.calculate(5, 3, "-")
        self.assertEqual(result, 2)

    def test_multiplication(self):
        result = self.calculator.calculate(4, 3, "*")
        self.assertEqual(result, 12)

    def test_division(self):
        result = self.calculator.calculate(10, 2, "/")
        self.assertEqual(result, 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.calculate(10, 0, "/")
    
    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate(2, 3, "%")

if __name__ == '__main__':
    unittest.main()