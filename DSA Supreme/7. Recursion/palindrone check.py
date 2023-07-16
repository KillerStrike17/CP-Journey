def palindrome(mystr, start, end):
    if start>=end:
        return True
    
    if mystr[start] ==mystr[end]:
        return palindrome(mystr, start+1,end-1)
    else:
        return False
    
mystr = "aaabacbaaa" 
print(palindrome(mystr,0,len(mystr)-1))