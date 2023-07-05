s = "abbaa"
def checkpalindrome(s,i,j):
    val = s[i:j+1]
    print(val)
    return val==val[::-1]


def check(s):
    i = 0
    j = len(s)-1

    while i<=j:
        if s[i]!=s[j]:
            return checkpalindrome(s,i+1,j) or checkpalindrome(s,i,j-1)
        else:
            i+=1
            j-=1
    return True

print(check(s))