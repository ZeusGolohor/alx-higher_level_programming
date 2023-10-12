#!/usr/bin/python3


def search_replace(my_list, search, replace):
    res = []
    for i in range(0, len(my_list)):
        if (my_list[i] == search):
            res.append(replace)
        else:
            res.append(my_list[i])
    return (res)
