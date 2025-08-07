import unittest
from main import average, median, sum_numbers, print_hi

class TestMain(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([1, 2, 3, 4, 5]), 3)
        self.assertEqual(average([]), 0)
        self.assertEqual(average([10]), 10)
        self.assertAlmostEqual(average([1, 2]), 1.5)

    def test_median(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([]), 0)
        self.assertEqual(median([7]), 7)
        self.assertEqual(median([2, 1]), 1.5)

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_numbers([]), 0)
        self.assertEqual(sum_numbers([10]), 10)

    def test_print_hi(self):
        # Test print_hi by capturing stdout
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_hi('Tester')
        sys.stdout = sys.__stdout__
        self.assertIn('Hi, Tester', captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()