#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """test max_integer function"""
    def setUp(self):
        """set list"""
        self.list_p = [1, 2, 3, 4]
        self.list_n = [-1, -2, -3, -4]
        self.list_l = list(range(1000))

    def test_max_integer(self):
        """test list"""
        self.assertEqual(max_integer(self.list_p), 4)
        self.assertEqual(max_integer(self.list_n), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(self.list_l), 999)
        self.assertEqual(max_integer([3, 3, 3, 3, 3]), 3)
        self.assertEqual(max_integer([-1, 2, 4, -4]), 4)
        self.assertIsInstance(max_integer(self.list_p), int)


if __name__ == "__main__":
    unittest.main()
