#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in range(len(i)):
            if (x < (len(i) - 1)):
                print('{:d}'.format(i[x]), end=' ')
            elif (x == (len(i) - 1)):
                print('{:d}'.format(i[x]))
    if (len(matrix) == 1):
        print()


if __name__ == '__main__':
    print_matrix_integer(matrix=[[]])
