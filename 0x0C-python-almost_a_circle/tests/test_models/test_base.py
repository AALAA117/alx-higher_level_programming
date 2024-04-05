"""test base Model"""
import unittest
import models
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """test base methods"""
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        """test number of objects and id"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base(None).id, 4)
        self.assertLess(Base().id, Base().id)
        self.assertIsNotNone(Base().id)
        self.assertIsInstance(Base().id, int)

    def test_to_json_string(self):
        """test for an object represented by json string :|"""
        obj1 = Rectangle(10, 7, 2, 8)
        a_dict = obj1.to_dictionary()
        json_string = '[{"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}]'
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([a_dict]), json_string)
        self.assertIsInstance(a_dict, dict)
        self.assertIsInstance(json_string, str)

    def test_from_json_string(self):
        """test for an object returned from json string :|"""
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_string = Rectangle.to_json_string(list_input)
        a_dict = Rectangle.from_json_string(json_string)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.from_json_string(json_string), a_dict)
        self.assertIsInstance(a_dict, list)
        self.assertIsInstance(json_string, str)

    def test_create(self):
        """
        test create an instance that can be
        used to access the calling class
        """
        obj1 = Rectangle(3, 5, 1)
        a_dict = obj1.to_dictionary()
        obj2 = Rectangle.create(**a_dict)
        self.assertIsInstance(obj2, Rectangle)
        self.assertIsNot(obj2, obj1)
        self.assertNotEqual(obj1, obj2)

    def test_save_to_file(self):
        """test JSON string representation of list_objs to a file"""


if __name__ == "__main__":
    unittest.main()
