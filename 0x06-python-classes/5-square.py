#!/usr/bin/python3
"""
The Square class is an empty class that is used
to demonstrate how classes works
"""


class Square:
    """
    The Square class is an empty class that is used
    to demonstrate how classes works
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, x):
        if isinstance(x, int) is False:
            raise TypeError("size must be an integer")
        else:
            if x < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = x

    def area(self):
        return (self.size ** 2)

    def my_print(self):
        num1 = num2 = self.size
        if num1 == 0:
            print()
        else:
            for i in range(num1):
                for x in range(num2):
                    print('#', end='')
                print()
