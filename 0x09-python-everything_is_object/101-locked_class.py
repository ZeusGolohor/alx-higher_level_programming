#!/usr/bin/python3
class LockedClass:
    def __init__(self):
        print(dir(self))
        for word in dir(self):
            if (word[0] != '_' and word[1] != '_'):
                print(word)
                if (word != 'first_name'):
                    raise AttributeError()
                    break
