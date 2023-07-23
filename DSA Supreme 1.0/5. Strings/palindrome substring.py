
def expandAroundIndex(s,i,j):
    count = 0
    while i>=0 and j<len(s) and s[i]==s[j]:
        count+=1
        i-=1
        j+=1
    return count


def countSubstring(s):
    s = "abc"
    count = 0
    n = len(s)-1

    for i in  range(len(s)):
        odds = expandAroundIndex(s,i,i)
        count +=odds

        evens = expandAroundIndex(s,i,i+1)
        count +=evens
    return count