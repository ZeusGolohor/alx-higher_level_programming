#!/usr/bin/python3
def islower(c):
    for i in range(65, 123):
        if (ord(c) == i):
            if (i >= 65 and i <= 90):
                return False
            elif (i >= 97 and i <= 122):
                return True
