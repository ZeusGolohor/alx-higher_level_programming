#!/usr/bin/python3
import sys
from calculator_1 import (
        add,
        sub,
        mul,
        div
        )


def r():
    if (len(sys.argv) != 4):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        for i in range(len(sys.argv)):
            a = int(sys.argv[1])
            op = sys.argv[2]
            b = int(sys.argv[3])
            if (op == '+'):
                print('{} + {} = {}'.format(a, b, add(a, b)))
                break
            elif (op == '-'):
                print('{} - {} = {}'.format(a, b, sub(a, b)))
                break
            elif (op == '*'):
                print('{} * {} = {}'.format(a, b, mul(a, b)))
                break
            elif (op == '/'):
                print('{} / {} = {}'.format(a, b, div(a, b)))
                break
            else:
                print('Unknown operator. Available operators: +, -, * and /')
                exit(1)
                break


if __name__ == '__main__':
    r()
