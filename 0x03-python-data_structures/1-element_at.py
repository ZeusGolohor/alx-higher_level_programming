#!/usr/bin/python3
def element_at(my_list, idx):
    if (int(idx) < 0 or int(idx) > len(my_list)):
        return None
    return (my_list[int(idx)])


if __name__ == '__main__':
    element_at(my_list, idx)
