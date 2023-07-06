st= list("leetcode")
vowels = "aeiou"
s = 0
e = len(st)-1

while s<=e:
    if st[s] in vowels and st[e] in vowels:
        st[s],st[e] = st[e],st[s]
        s +=1
        e -=1
    
    elif st[s] not in vowels:
        s+=1
    elif st[e] not in vowels:
        e-=1
    else:
        s+=1
        e-=1
        
print("".join(st))

