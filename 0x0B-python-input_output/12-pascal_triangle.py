#!/usr/bin/python3
"""
This module is used to return a list
of lists of integers representing the
Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    This method is used to a list
    of lists of integers representing
    the Pascal’s triangle of n.
    """
    i = -1
    pas_list = []
    if (n <= 0):
        return (pas_list)
    if (n >= 1):
        pas_list.append([1])
        i = i + 1
        n = n - 1
    if (n >= 2):
        pas_list.append([1, 1])
        i = i + 1
        n = n - 1
    for x in range(n):
        new_list = []
        new_list.append(1)
        y = 0
        while (y < len(pas_list[i])):
            if ((y + 1) < len(pas_list[i])):
                new_list.append(pas_list[i][y] + pas_list[i][y + 1])
            y = y + 1
        new_list.append(1)
        pas_list.append(new_list)
        new_list = []
        i = i + 1
    return (pas_list)
