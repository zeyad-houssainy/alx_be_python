import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.
    
    def test_subtraction(self):
        """test_subtraction"""
        self.assertEqual(self.calc.subtract(2,3), -1)
        self.assertEqual(self.calc.subtract(2,0), 2)

    def test_multiply(self):
        """Test the multiply method"""
        self.assertEqual(self.calc.multiply(5,5), 25)

    def test_divide(self):
        """Test the divide method"""
        self.assertEqual(self.calc.divide(10,2), 5)
        self.assertIsNone(self.calc.divide(10, 0))
        with self.assertRaises(TypeError):
            self.calc.divide(10, "zeyad")


# Remember to write additional test methods for subtract, multiply, and divide.

