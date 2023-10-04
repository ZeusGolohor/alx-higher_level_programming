def prt(prt):
    print('{}'.format(prt), end='')


def uppercase(str):
    for i in str:
        if ((ord(i) >= 65 and ord(i) <= 90) or ord(i) == 32 or ord(i) == 44 or
                (ord(i) >= 48 and ord(i) <= 57)):
            prt(i)
        elif (ord(i) >= 97 and ord(i) <= 122):
            prt(chr(ord(i) - 32))
    print()
