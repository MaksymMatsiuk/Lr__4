import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):


    def test_exponentiation_positive_numbers(self):
        calc = Calculator(2, 3)
        result = calc.exp()
        self.assertEqual(result, 8)

    def test_exponentiation_negative_numbers(self):
        calc = Calculator(-2, 3)
        result = calc.exp()
        self.assertEqual(result, -8)

    def test_exponentiation_mixed_numbers(self):
        calc = Calculator(-2, -3)
        result = calc.exp()
        self.assertEqual(result, -0.125)

    def test_gcd_positive_numbers(self):
        calc = Calculator(54, 24)
        result = calc.gcd()
        self.assertEqual(result, 6)

    def test_gcd_negative_numbers(self):
        calc = Calculator(-54, 24)
        result = calc.gcd()
        self.assertEqual(result, 6)

    def test_gcd_mixed_numbers(self):
        calc = Calculator(-54, -24)
        result = calc.gcd()
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()