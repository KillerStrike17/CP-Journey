val = 123456789

def printNumbers(val):
    if val == 0:
        return
    
    rem = val%10
    

    val = val//10
    printNumbers(val)
    print(rem,end="")

printNumbers(val)