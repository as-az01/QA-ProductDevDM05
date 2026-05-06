import unittest
from calculator import Calculator

class TestOperations(unittest.TestCase):
        def setUp(self):
             self.calc = Calculator(8,2)

        def test_sum(self):
            calc = Calculator(8, 2)
            self.assertEqual(calc.get_sum(), 10, "The answer was not 10")

        def test_diff(self):
            calc = Calculator(8, 2)
            self.assertEqual(calc.get_diff(), 6, "The answer was not 6")

        def test_prod(self):
            calc = Calculator(8, 2)
            self.assertEqual(calc.get_prod(), 16, "The answer was not 16")

        def test_div(self):
            calc = Calculator(8, 2)
            self.assertEqual(calc.get_div(), 4, "The answer was not 14")

if __name__ == "__main__":
      unittest.main()