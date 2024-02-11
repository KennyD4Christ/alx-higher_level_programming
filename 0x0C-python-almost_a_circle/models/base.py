#!/usr/bin/python3
"""Module defining Base class"""
import json
import csv
import turtle


class Base:
    """
    Base class for managing id attribute

    Attributes:
        __nb_objects (int): A private class attribute to keep track of
        the number of objects created.

    Methods:
        __init__: Initializes a new instance of the Base class.
        to_json_string: Static method to convert a list of dictionaries
        into a JSON string representation.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize Base instance with optional id
        Args:
            id (int): An optional identifier for the instance.
            If provided, it will be assigned to the 'id' attribute.
            If not provided, a unique identifier will be generated
            using the __nb_objects class attribute.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries into a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.
        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save list_objs to a file in JSON format."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            list_of_dicts = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(list_of_dicts)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Return a list from JSON string representation.
        Args:
            json_string (str): A string representing a list of dictionaries
            in JSON format.

        Returns:
            list: List represented by json_string.
        """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            from models.rectangle import Rectangle
            dummy_instance = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            from models.square import Square
            dummy_instance = Square(1)
        else:
            return None
        for key, value in dictionary.items():
            if key in ['x', 'y']:
                dictionary[key] = int(value)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                list_of_dicts = cls.from_json_string(json_string)
                return [cls.create(**dict_obj) for dict_obj in list_of_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                loaded_objs = []
                for d in list_dicts:
                    print("Loaded dictionary:", d)
                    loaded_objs.append(cls.create(**d))
                return loaded_objs
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")
        turt.color("#ffffff")

        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(int(rect.x), int(rect.y))
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(int(sq.x), int(sq.y))
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
