s = "ab-cd_"
mystr = list(s)
def revereseOnlyLetters(mystr):
    s =0
    e = len(mystr)-1 
    
    while(s<=e):
        if mystr[s].isalpha() and mystr[e].isalpha():
            mystr[s],mystr[e] = mystr[e],mystr[s]
            s +=1
            e -=1
        elif mystr[s].isalpha():
            e -=1
        elif mystr[e].isalpha():
            s +=1
        else:
            s +=1
            e -=1
    return mystr

mystr = revereseOnlyLetters(mystr)
print("".join(mystr))
        