#!/usr/bin/python3
"""Defines unittests for base.py."""


import os
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Reset __nb_objects counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_incrementation(self):
        """Test id incrementation when id is not provided"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_assignment(self):
        """Test id assignment when id is provided"""
        b1 = Base(10)
        b2 = Base(20)
        self.assertEqual(b1.id, 10)
        self.assertEqual(b2.id, 20)

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list."""
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string(self):
        """Test to_json_string with a non-empty list."""
        input_list = [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Alice'}]
        expected_result = '[{"id": 1, "name": "John"}, ' \
                          '{"id": 2, "name": "Alice"}]'
        result = Base.to_json_string(input_list)
        self.assertEqual(result, expected_result)

    @classmethod
    def setUpClass(cls):
        """Create instances for testing."""
        cls.r1 = Rectangle(1, 2)
        cls.r2 = Rectangle(3, 4)

    def test_save_to_file_rectangle(self):
        """Test save_to_file method with Rectangle instances."""
        Rectangle.save_to_file([self.r1, self.r2])
        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))
        with open(filename, mode='r') as file:
            content = file.read()
            expected_content = (
                '[{"id":1,"width":1,"height":2,"x":0,"y":0},'
                '{"id":2,"width":3,"height":4,"x":0,"y":0}]'
            )
            expected_content = (
                expected_content
                .replace(" ", "")
                .replace("\n", "")
            )
            content_dict = json.loads(content)
            expected_dict = json.loads(expected_content)
            # Sort both lists of dictionaries based on the 'id' key
            content_dict_sorted = sorted(content_dict, key=lambda x: x['id'])
            expected_dict_sorted = sorted(expected_dict, key=lambda x: x['id'])
            # Convert sorted dictionaries back to JSON strings for comparison
            content_sorted = json.dumps(content_dict_sorted)
            expected_sorted = json.dumps(expected_dict_sorted)
            self.assertEqual(content_sorted, expected_sorted)

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string(self):
        """Test from_json_string with a non-empty JSON string."""
        input_string = ('[{"id": 1, "name": "John"}, '
                        '{"id": 2, "name": "Alice"}]')
        expected_result = [
            {'id': 1, 'name': 'John'},
            {'id': 2, 'name': 'Alice'}
        ]
        result = Base.from_json_string(input_string)
        self.assertEqual(result, expected_result)

    def test_create_rectangle(self):
        """Test create method with Rectangle class."""
        r1_dictionary = {'width': 5, 'height': 10, 'x': 2, 'y': 4}
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 4)
        self.assertIsInstance(r2, Rectangle)

    def test_create_square(self):
        """Test create method with Square class."""
        s1_dictionary = {'size': 7, 'x': 1, 'y': 2}
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(s2.size, 7)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 2)
        self.assertIsInstance(s2, Square)

    def test_load_from_file_rectangle(self):
        """Test load_from_file method with Rectangle class."""
        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)
        self.assertFalse(os.path.exists(filename))

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles, list)
        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertEqual(rectangles[0].width, 10)
        self.assertEqual(rectangles[0].height, 7)
        self.assertEqual(rectangles[0].x, 2)
        self.assertEqual(rectangles[0].y, 8)

        self.assertEqual(rectangles[1].width, 2)
        self.assertEqual(rectangles[1].height, 4)
        self.assertEqual(rectangles[1].x, 0)
        self.assertEqual(rectangles[1].y, 0)

    def test_load_from_file_square(self):
        """Test load_from_file method with Square class."""
        filename = "Square.json"
        if os.path.exists(filename):
            os.remove(filename)
        self.assertFalse(os.path.exists(filename))

        s1 = Square(5)
        s2 = Square(9, 1, 3)
        Square.save_to_file([s1, s2])

        squares = Square.load_from_file()
        self.assertIsInstance(squares, list)
        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertEqual(squares[0].size, 5)
        self.assertEqual(squares[0].x, 0)
        self.assertEqual(squares[0].y, 0)

        self.assertEqual(squares[1].size, 9)
        self.assertEqual(squares[1].x, 1)
        self.assertEqual(squares[1].y, 3)

    class TestBase_save_to_file_csv(unittest.TestCase):
        """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""

        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file__csv_cls_name(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

    class TestBase_load_from_file_csv(unittest.TestCase):
        """Unittests for testing load_from_file_csv method of Base class."""

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_rectangle_types(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_from_file_csv_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == '__main__':
    unittest.main()
