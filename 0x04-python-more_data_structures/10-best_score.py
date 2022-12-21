#!/usr/bin/python3

def best_score(a_dictionary):
    best = 0
    name = ''
    if a_dictionary is None or len(a_dictionary) == 0:
        return (None)
    for i in list(a_dictionary):
        if (a_dictionary[i] > best):
            best = a_dictionary[i]
            name = i
    return (name)
