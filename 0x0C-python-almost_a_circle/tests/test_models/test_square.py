#!/usr/bin/python3
"""Unit tests for Square class"""

import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """
    Test cases for Square class
    """

    def test_str(self):
        """Test __str__ method"""
        square = Square(5, 1, 2, 10)
        self.assertEqual(str(square), "[Square] (10) 1/2 - 5")

    def test_size_getter(self):
        """Test size getter"""
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        """Test size setter"""
        square = Square(5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_update_args(self):
        """Test update method with *args"""
        square = Square(5, 1, 1, 1)
        square.update(10, 20, 30, 40)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_update_kwargs(self):
        """Test update method with **kwargs"""
        square = Square(5, 1, 1, 1)
        square.update(size=20, id=10, y=40, x=30)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 20)
        self.assertEqual(square.x, 30)
        self.assertEqual(square.y, 40)

    def test_update_no_keyword(self):
        """Test update method with no-keyword arguments."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_keyword(self):
        """Test update method with keyword arguments."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(id=10, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_update_mixed(self):
        """Test update method with mixed arguments."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(10, width=20, height=30, x=40, y=50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(5, 2, 3, 1)
        s_dict = s.to_dictionary()
        self.assertEqual(s_dict, {'id': 1, 'size': 5, 'x': 2, 'y': 3})
