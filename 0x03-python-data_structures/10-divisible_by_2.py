#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if (len(my_list) == 0):
        return (my_list)

    new_list = []
    for i in range(len(my_list)):
        if ((int(my_list[i]) % 2) == 0):
            new_list.append(True)
        else:
            new_list.append(False)

    return (new_list)


if __name__ == '__main__':
    divisible_by_2(my_list=[])
