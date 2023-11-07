#!/usr/bin/python3
"""
This module is used to add all arguments
to a Python list, and then save them to a file.
"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """
    This method is used to add all arguments
    to a Python list, and then save them to a file.
    """
    word_len = 0
    my_list = []
    try:
        old_list = load_from_json_file("add_item.json")
        if old_list[0] == []:
            my_list.append(old_list[1:])
        else:
            my_list.extend(old_list)
    except Exception:
        pass
    for word in sys.argv:
        word_len = word_len + 1
        if (word_len != 1):
            my_list.append(word)

    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    main()
