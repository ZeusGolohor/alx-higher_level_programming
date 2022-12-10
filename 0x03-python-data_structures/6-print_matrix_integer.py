#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        c = 0
        for x in i:
            if (c != 2):
                print('{:d}'.format(x), end=' ')
            else:
                print('{:d}'.format(x), end='')
            c += 1
        print()


if __name__ == '__main__':
    print_matrix_integer(matrix=[[]])
