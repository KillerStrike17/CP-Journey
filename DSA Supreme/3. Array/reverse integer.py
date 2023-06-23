def reverseInteger(n:int)->int:
    if n<0:
        temp = str(n)[1:]
        return -1*int(temp[::-1])
    else:
        temp = str(n)
        return int(temp[::-1])
    
print(reverseInteger(123))
print(reverseInteger(-123))


def reverseInteger(n:int)->int:
    ans = 0
    rem = 0
    check = True
    if n <0:
        check = False
        n = n*-1
    while n>0:
        rem = n%10
        ans=ans*10 + rem 
        n = n//10
    if check:
        return ans
    else:
        return ans*-1

print(reverseInteger(123))
print(reverseInteger(-123))
