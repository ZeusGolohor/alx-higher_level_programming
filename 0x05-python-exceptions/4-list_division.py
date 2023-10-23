#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    try:
        for l1, l2 in zip(my_list_1, my_list_2):
            if (isinstance(l1, str) is False and isinstance(l2, str)
                    is False and i < list_length):
                if (l2 == 0):
                    print('{}'.format('division by 0'))
                    new_list.append(0)
                    i += 1
                else:
                    new_list.append(l1/l2)
                    i += 1
            elif i < list_length:
                print('{}'.format('wrong type'))
                new_list.append(0)
                i += 1

        while (i < list_length):
            print('{}'.format('out of range'))
            new_list.append(0)
            i += 1
    except Exception:
        raise
    finally:
        return (new_list[:list_length])
