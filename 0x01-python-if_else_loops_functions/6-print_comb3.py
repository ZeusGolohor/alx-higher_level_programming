#!/usr/bin/python3
for f in range(0, 9):
    for s in range(1, 10):
        if (f != s and f < s):
            if ('{}{}'.format(f, s) != '89'):
                print('{}{}'.format(f, s), end=', ')
            elif ('{}{}'.format(f, s) == '89'):
                print('{}{}'.format(f, s))
