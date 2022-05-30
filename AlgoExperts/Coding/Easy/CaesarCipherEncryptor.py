def caesarCipherEncryptor(string, key):
    # Write your code here.
    if key > 25:
        key %= 26
    mystring = ''
    for _ in list(string):
        # print(_)
        x = ord(_)+key
        if x > 122:
            print(chr(96 + x-122), end='')
            mystring += chr(96 + x-122)
        else:
            print(chr(x), end='')
            mystring += chr(x)
    # print('')
    return mystring
    # print(97+25)
    # pass
