s = "ababd"
def isPalindrome(s,i,j):
    while(i<j):
        if s[i] !=s[j]:
            return False
        i+=1
        j-=1
    return True
        

ans = ""

for i in range(len(s)):
    for j in range(i,len(s)):
        if isPalindrome(s,i,j):
            print("here")
            mystring = s[i:j+1]
            if len(ans)<len(mystring):
                ans = mystring

print(ans)