import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        # Arrange
        calc = Calculator(3, 5)

        # Act
        result = calc.add()

        # Assert
        self.assertEqual(result, 8, "Addition failed")

    def test_addition_negative_numbers(self):
        # Arrange
        calc = Calculator(-3, 5)

        # Act
        result = calc.add()

        # Assert
        self.assertEqual(result, 2, "Addition of negative numbers failed")

    def test_addition_float_numbers(self):
        # Arrange
        calc = Calculator(3.5, 2.5)

        # Act
        result = calc.add()

        # Assert
        self.assertEqual(result, 6.0, "Addition of float numbers failed")

    def test_addition_zero(self):
        # Arrange
        calc = Calculator(0, 0)

        # Act
        result = calc.add()

        # Assert
        self.assertEqual(result, 0, "Addition of zero failed")

    def test_subtraction_positive_numbers(self):
        calc = Calculator(5, 3)
        result = calc.sub()
        self.assertEqual(result, 2)

    def test_subtraction_negative_numbers(self):
        calc = Calculator(-5, -3)
        result = calc.sub()
        self.assertEqual(result, -2)

    def test_subtraction_mixed_numbers(self):
        calc = Calculator(5, -3)
        result = calc.sub()
        self.assertEqual(result, 8)

    def test_multiplication_positive_numbers(self):
        calc = Calculator(5, 3)
        result = calc.mul()
        self.assertEqual(result, 15)

    def test_multiplication_negative_numbers(self):
        calc = Calculator(-5, -3)
        result = calc.mul()
        self.assertEqual(result, 15)

    def test_multiplication_mixed_numbers(self):
        calc = Calculator(5, -3)
        result = calc.mul()
        self.assertEqual(result, -15)

    def test_division_positive_numbers(self):
        calc = Calculator(6, 3)
        result = calc.div()
        self.assertEqual(result, 2)

    def test_division_negative_numbers(self):
        calc = Calculator(-6, -3)
        result = calc.div()
        self.assertEqual(result, 2)

    def test_division_mixed_numbers(self):
        calc = Calculator(6, -3)
        result = calc.div()
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()
