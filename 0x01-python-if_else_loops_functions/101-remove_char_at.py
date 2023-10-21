#!/usr/bin/python3

def remove_char_at(str, n):
    st = ""
    for i in range(len(str)):
        if i != n:
            st += str[i]
    return (st)
