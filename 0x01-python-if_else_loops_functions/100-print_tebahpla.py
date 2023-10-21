#!/usr/bin/python3

def printAlpha():
    lower = 0
    for char in range(ord('Z'), ord('A') - 1, -1):
        if (lower == 0):
            print("{}".format(chr(char).lower()), end="")
            lower = 1
        else:
            print("{}".format(chr(char)), end="")
            lower = 0


if __name__ == "__main__":
    printAlpha()
