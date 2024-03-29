#!/usr/bin/python3
"""test rectangle model"""
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """test rectangle_model"""
    def setUp(self):
        self.obj1 = Rectangle(3, 2)
        self.obj2 = Rectangle(8, 7, 0, 0, 12)
        self.obj3 = Rectangle(5, 5, 1)

    def tets_area(self):
        self.assertEqual(self.obj1.area(), 6)
        self.assertEqual(self.obj2.area(), 56)

    def test_width_setter(self):
        self.assertEqual(self.obj1.area(), 6)
        self.assertEqual(self.obj2.area(), 56)
        with self.assertRaises(ValueError) as e:
            self.obj1.width = -1
        msg1 = "width must be > 0"
        self.assertEqual(str(e.exception), msg1)
        with self.assertRaises(TypeError) as e:
            self.obj1.width = "width"
        msg2 = "width must be an integer"
        self.assertEqual(str(e.exception), msg2)

    def test_height_setter(self):
        self.assertEqual(self.obj1.area(), 6)
        self.assertEqual(self.obj2.area(), 56)
        with self.assertRaises(ValueError) as e:
            self.obj1.height = -1
        msg1 = "height must be > 0"
        self.assertEqual(str(e.exception), msg1)
        with self.assertRaises(TypeError) as e:
            self.obj1.height = "height"
        msg2 = "height must be an integer"
        self.assertEqual(str(e.exception), msg2)

    def test_id(self):
        self.assertNotEqual(self.obj1.id, self.obj2.id)
        self.assertEqual(self.obj2.id, 12)

    def test_str(self):
        str_msg = "[Rectangle] ({}) {}/{} - {}/{}".format(
                  self.obj1.id, self.obj1.x, self.obj1.y,
                  self.obj1.width, self.obj1.height)
        self.assertEqual(str(self.obj1), str_msg)


if __name__ == "__main__":
    unittest.main()
