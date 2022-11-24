import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(4, 4), 8)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 4), 1)

    # Handle both paths of divide, we need tests for raising an
    # error and for a successful test!
    def test_div(self):
        self.assertEqual(calc.divide(1, 1), 1)
        with self.assertRaises(ArithmeticError):
            self.assertEqual(calc.divide(1, 0), 11)

    def test_multiply(self):
        self.assertEqual(calc.multiply(4, 4), 16)


if __name__ == '__main__':
    unittest.main()
