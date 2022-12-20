#!/usr/bin/python3

def check(search, value):
    if (search == value):
        return (True)
    else:
        return (False)


def search_replace(my_list, search, replace):
    newlist = []
    for i in my_list:
        if (check(search, i)):
            newlist.append(89)
        else:
            newlist.append(i)
    return (newlist)
