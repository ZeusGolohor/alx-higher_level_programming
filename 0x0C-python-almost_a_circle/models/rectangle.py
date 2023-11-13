#!/usr/bin/python3
"""
This module is used to showcase inheritance from
the base class.
"""
from models.base import Base


class Rectangle(Base):
    """
    This class is used to showcase inheritance from
    the base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __repr__(self):
        """
        Returns the instance representation for developers.
        """
        return f'<id: {self.id}, width: {self.width}, height:\
                {self.height}, x: {self.x}, y: {self.y}>'

    @property
    def width(self):
        """
        Used to get width details
        """
        return (self.__width)

    @width.setter
    def width(self, width):
        """
        Used to set the width details.
        """
        if (isinstance(width, int) is False):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Used to get height details.
        """
        return (self.__height)

    @height.setter
    def height(self, height):
        """
        Used to set the height details.
        """
        if (isinstance(height, int) is False):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Used to get x details.
        """
        return (self.__x)

    @x.setter
    def x(self, x):
        """
        Used to set x details.
        """
        if (isinstance(x, int) is False):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Used to get y details.
        """
        return (self.__y)

    @y.setter
    def y(self, y):
        """
        Used to set y details.
        """
        if (isinstance(y, int) is False):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        used to get the area of the rectangle instance.
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Used to print to the Rectangle
        instance with the character #.
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Used to represent the string
        representation of an object
        that is human-readable.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """
        This method is used to update the Rectangle
        class.
        """
        if (len(args) != 0):
            # id update
            try:
                setattr(self, "id", args[0])
            except IndexError:
                pass
            # width update
            try:
                setattr(self, "width", args[1])
            except IndexError:
                pass
            # height update
            try:
                setattr(self, "height", args[2])
            except IndexError:
                pass
            # x update
            try:
                setattr(self, "x", args[3])
            except IndexError:
                pass
            # y update
            try:
                setattr(self, "y", args[4])
            except IndexError:
                pass
        else:
            # dynamic update for all available key/value pairs
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        Rectangle instance to dictionary representation.
        """
        new_json = {}
        for word in dir(self):
            if word[0] != "_":
                if (isinstance(getattr(self, word), int) is True):
                    new_json[word] = getattr(self, word)
        return (new_json)
