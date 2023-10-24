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
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
        self.__count_lim = 0

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
            if (self.__position[1] > self.__count_lim):
                for i in range(self.__position[1]):
                    print('')

            for i in range(num1):
                for x in range(self.__position[0]):
                    print(' ', end='')

                for x in range(num2):
                    print('#', end='')
                print()

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, x):
        if (len(x) < 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(x[0], int) is False or isinstance(x[1], int) is False):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif ((x[0] < 0) or (x[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = x

