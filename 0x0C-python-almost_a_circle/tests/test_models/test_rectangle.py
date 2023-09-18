#!/usr/bin/python3
""" Test Rectangle Module """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Rectangle model test class """
    def setUp(self):
        Base.__Base__nb_objects = 0

    def test_rectangle_instance(self):
        """ Test square instance """
        r0 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r0.id, 5)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        self.assertEqual(r0.x, 3)
        self.assertEqual(r0.y, 4)
        self.assertEqual(r0.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        self.assertEqual(r0.area(), 2)

        test1 = {'x': 3, 'y': 4, 'id': 5, 'height': 2, 'width': 1}
        self.assertEqual(r0.to_dictionary(), test1)

        r0.update()
        self.assertEqual(r0.__str__(), "[Rectangle] (5) 3/4 - 1/2")

        r0.update(89)
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r0.update(89, 1)
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r0.update(89, 1, 2)
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r0.update(89, 1, 2, 3)
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r0.update(89, 1, 2, 3, 4)
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r0.update(**{'id': 89})
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r0.update(**{'id': 89, 'width': 1})
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r0.update(**{'id': 89, 'witdh': 1, 'height': 2})
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r0.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r0.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r0.__str__(), "[Rectangle] (89) 3/4 - 1/2")

        r0dictionary = r0.to_dictionary()
        r1 = Rectangle.create(**r0dictionary)
        self.assertIsNot(r0, r1)

    def test_typeError(self):
        """ Test TypeError """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, "4")

    def test_valueError(self):
        """ Test ValueError """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 2, 3, -4)


if __name__ == '__main__':
    unittest.main()
