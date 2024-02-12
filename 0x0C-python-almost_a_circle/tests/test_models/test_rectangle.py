#!/usr/bin/python3
"""Defines unittests for models/rectangle.py."""


import unittest
import io
import unittest.mock


from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_constructor(self):
        """Test constructor"""
        r1 = Rectangle(10, 20, 1, 2, 100)
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 20)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 2)

    def test_getters_and_setters(self):
        """Test getters and setters"""
        r1 = Rectangle(10, 20, 1, 2, 100)
        r1.width = 30
        r1.height = 40
        r1.x = 5
        r1.y = 6
        self.assertEqual(r1.width, 30)
        self.assertEqual(r1.height, 40)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 6)

    def test_invalid_width(self):
        """Test invalid width"""
        with self.assertRaises(TypeError):
            Rectangle("invalid", 20, 1, 2)

        with self.assertRaises(ValueError):
            Rectangle(-10, 20, 1, 2)

    def test_invalid_height(self):
        """Test invalid height"""
        with self.assertRaises(TypeError):
            Rectangle(10, "invalid", 1, 2)

        with self.assertRaises(ValueError):
            Rectangle(10, -20, 1, 2)

    def test_invalid_x(self):
        """Test invalid x"""
        with self.assertRaises(TypeError):
            Rectangle(10, 20, "invalid", 2)

        with self.assertRaises(ValueError):
            Rectangle(10, 20, -1, 2)

    def test_invalid_y(self):
        """Test invalid y"""
        with self.assertRaises(TypeError):
            Rectangle(10, 20, 1, "invalid")

        with self.assertRaises(ValueError):
            Rectangle(10, 20, 1, -2)

    def test_area(self):
        """Test area calculation"""
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

    def test_display(self):
        """Test display method"""
        r = Rectangle(3, 2, 2, 1)
        expected_output = "\n  ###\n  ###\n"
        with io.StringIO() as fake_stdout:
            with unittest.mock.patch('sys.stdout', new=fake_stdout):
                r.display()
                self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test __str__ method"""
        r = Rectangle(3, 2, 1, 1, 100)
        self.assertEqual(str(r), "[Rectangle] (100) 1/1 - 3/2")

    def test_update(self):
        """Test update method"""
        r = Rectangle(3, 2)
        r.update(100, 5, 10, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (100) 2/3 - 5/10")
