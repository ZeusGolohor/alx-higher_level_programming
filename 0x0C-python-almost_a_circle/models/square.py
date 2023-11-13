#!/usr/bin/python3
"""
This module illustrates a class that
inherites from another class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class illustrate inheritance from
    another class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Class constructor.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Class object representation in human
        reable form.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.height))

    @property
    def size(self):
        """
        Used to return the size of the square.
        """
        return (self.width)

    @size.setter
    def size(self, size):
        """
        Used to update the size of the square.
        """
        setattr(self, "width", size)
        setattr(self, "height", size)

    def update(self, *args, **kwargs):
        """
        Used to update the square atrributes.
        """
        if (len(args) != 0):
            # id update
            try:
                setattr(self, "id", args[0])
            except IndexError:
                pass
            # size update
            try:
                setattr(self, "width", args[1])
                setattr(self, "height", args[1])
            except IndexError:
                pass
            # x update
            try:
                setattr(self, "x", args[2])
            except IndexError:
                pass
            # y update
            try:
                setattr(self, "y", args[3])
            except IndexError:
                pass
        else:
            if ((len(kwargs) == 1) and ("size" in kwargs)):
                setattr(self, "width", kwargs["size"])
                setattr(self, "height", kwargs["size"])
                setattr(self, "x", 0)
                setattr(self, "y", 0)
            else:
                # dynamic kwargs update
                for key in kwargs:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        Square instance to dictionary representation.
        """
        new_json = {}
        for word in dir(self):
            if ((word[0] != "_") and (word not in {"height", "width"})):
                if (isinstance(getattr(self, word), int) is True):
                    new_json[word] = getattr(self, word)
        return (new_json)
