from collections import Counter


def firstNonRepeatingCharacter(string):
    # Write your code here.
    val = -1
    check = -1
    x = list(string)
    print(x)
    mydict = Counter(x)
    print(mydict)
    for _ in mydict.keys():
        if mydict[_] == 1:
            check = _
            break
    print("Check:", check)
    if check != -1:
        for _ in range(len(x)):
            print(_)
            print
            if check == x[_]:
                val = _
                break
    return val
