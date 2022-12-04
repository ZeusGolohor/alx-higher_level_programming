#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) >= 65 and ord(i) <= 90):
            print('{}'.format(i), end='')
        elif (ord(i) >= 97 and ord(i) <= 122):
            print('{}'.format(chr(ord(i) - 32)), end='')
        elif (ord(i) == 32):
            print(' ', end='')
        else:
            print('{}'.format(i), end='')
    print()
