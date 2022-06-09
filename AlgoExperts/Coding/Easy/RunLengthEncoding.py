def runLengthEncoding(string):
    # Write your code here.
    x = list(string)
    print(x)
    val = 1
    check = x[0]
    s = ''
    for _ in x[1:]:
        # print(_)
        print("Check:", check, _)
        if check == _:
            val += 1
            if val == 9:
                s += str(val) + check
                val = 0
        else:
            if val != 0:
                s += str(val) + check
                check = _
                val = 1
            else:
                check = _
                val += 1
    s += str(val) + check
    print(s)
    return s
