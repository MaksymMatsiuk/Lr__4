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

    def test_lcm_positive_numbers(self):
        calc = Calculator(6, 9)
        result = calc.lcm()
        self.assertEqual(result, 18)

    def test_lcm_negative_numbers(self):
        calc = Calculator(-12, -18)
        result = calc.lcm()
        self.assertEqual(result, 36)

    def test_lcm_mixed_numbers(self):
        calc = Calculator(8, -12)
        result = calc.lcm()
        self.assertEqual(result, 24)

    def test_lcm_one_zero(self):
        calc = Calculator(0, 7)
        result = calc.lcm()
        self.assertEqual(result, 0)

    def test_lcm_both_zeros(self):
        calc = Calculator(0, 0)
        result = calc.lcm()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()