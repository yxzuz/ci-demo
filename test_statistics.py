"""Unittest for statistics.py."""
from unittest import TestCase
from statistics import variance, stdev, average
from math import sqrt


class StatisticsTest(TestCase):

    def test_variance_typical_values(self):
        """Variance of typical values."""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_non_integers(self):
        """Variance should work with decimal values."""
        # variance([x,y,z]) == variance([x+d,y+d,z+d]) for any d
        self.assertAlmostEqual(4.0, variance([0.1, 4.1]))
        # variance([0,4,4,8]) == 8
        self.assertAlmostEqual(8.0, variance([0.1, 4.1, 4.1, 8.1]))

    def test_stdev(self):
        """Test for Standard deviation."""
        # standard deviation of a single value should be zero
        self.assertEqual(0.0, stdev([10.0]))
        # simple test
        self.assertEqual(2.0, stdev([1, 5]))
        # variance([0, 0.5, 1, 1.5, 2.0]) is 0.5
        self.assertEqual(sqrt(0.5), stdev([0, 0.5, 1, 1.5, 2]))

    def test_avg_positive(self):
        """Test for average function"""
        self.assertEqual(average([1,2,3,4,5]), 3)

    # def test_avg_two_vals(self):
    #     """Test for average with two values"""
    #     self.assertEqual(average([2, 3]), 2.5)

    # def test_avg_negative(self):
    #     self.assertEqual(average([-1,-2,-3,-4]), -2.5)
    #
    # def test_avg_no_len(self):
    #     with self.assertRaises(ValueError) as c:
    #         average([])
    #     self.assertEqual(str(c.exception), "List must contain at least one value")


# if __name__ == '__main__':
#     import unittest
#     unittest.main(verbosity=1)
