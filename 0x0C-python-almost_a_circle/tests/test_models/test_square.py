#!/usr/bin/python3
""" Test Square Module """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Square model test class """
    def setUp(self):
        Base.__Base__nb_objects = 0

    def test_square_instance(self):
        """ Test square instance """
        s0 = Square(1, 2, 3, 4)
        self.assertEqual(s0.id, 4)
        self.assertEqual(s0.width, 1)
        self.assertEqual(s0.height, 1)
        self.assertEqual(s0.x, 2)
        self.assertEqual(s0.y, 3)
        self.assertEqual(s0.__str__(), "[Square] (4) 2/3 - 1")
        self.assertEqual(s0.area(), 1)

        test1 = {'id': 4, 'x': 2, 'size': 1, 'y': 3}
        self.assertEqual(s0.to_dictionary(), test1)

        s0.update()
        self.assertEqual(s0.__str__(), "[Square] (4) 2/3 - 1")

        s0.update(89)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

        s0.update(89, 1)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

        s0.update(89, 1, 2)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

        s0.update(89, 1, 2, 3)
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

        s0.update(**{'id': 89})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

        s0.update(**{'id': 89, 'size': 1})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

        s0.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

        s0.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s0.__str__(), "[Square] (89) 2/3 - 1")

        s0dictionary = s0.to_dictionary()
        s1 = Rectangle.create(**s0dictionary)
        self.assertIsNot(s0, s1)

    def test_typeError(self):
        """ Test TypeError """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_valueError(self):
        """ Test ValueError """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)


if __name__ == '__main__':
    unittest.main()
