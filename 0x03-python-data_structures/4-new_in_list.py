#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if ((int(idx) < 0) or (int(idx) > (len(my_list) - 1))):
        return (my_list[:])
    b = my_list[:]
    b[int(idx)] = element
    return (b)


if __name__ == '__main__':
    new_in_list(my_list, idx, element)
