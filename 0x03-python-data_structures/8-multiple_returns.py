#!/usr/bin/python3
def multiple_returns(sentence):
    if (len(sentence) == 0):
        return (0, None)

    return (len(sentence), sentence[0])


if __name__ == '__main__':
    multiple_returns(sentence)
