#!/usr/bin/python3
def pow(a, b):
    i = 1
    if (b >= 0):
        for x in range(b):
            i *= a

        return (i)
    elif (b < 0):
        for x in range(abs(b)):
            i *= a

        return (1/i)

