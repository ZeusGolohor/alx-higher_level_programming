#!/usr/bin/python3
"""
this module is used to divide all element of the matrix
"""


def matrix_divided(matrix, div):
    """
    this function is used to divide all the element of the matrix
    """
    if (matrix is None):
        raise TypeError('matrix must be a matrix ' +
                        '(list of lists) of integers/floats')
    if (div is None):
        raise TypeError('div must be a number')
    max_len = len(matrix[0])
    temp = []
    perm = []
    for i in matrix:
        if (len(i) is not max_len):
            raise TypeError('Each row of the matrix ' +
                            'must have the same size')
        else:
            temp = []
            for x in i:
                if ((isinstance(x, int) is False) and
                        (isinstance(x, float) is False)):
                    raise TypeError('matrix must be a matrix ' +
                                    '(list of lists) of integers/floats')
                if ((isinstance(div, int) is False) and
                        (isinstance(div, float) is False)):
                    raise TypeError('div must be a number')
                if (div == 0):
                    raise ZeroDivisionError('division by zero')
                temp.append(float('{:.2f}'.format(x/div)))
            perm.append(temp)
    return (perm)
