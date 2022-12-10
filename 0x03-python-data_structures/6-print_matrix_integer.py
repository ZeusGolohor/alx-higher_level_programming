#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for x in range(len(i)):
            if (x < (len(i) - 1)):
                print('{:d}'.format(i[x]), end=' ')
            elif (x == (len(i) - 1)):
                print('{:d}'.format(i[x]))
    if (len(matrix) > 0):
        if (len(matrix[0]) != 0):
            print()
        #print(len(matrix[0]))


if __name__ == '__main__':
    print_matrix_integer(matrix=[[]])
