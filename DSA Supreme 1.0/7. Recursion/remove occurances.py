s = "daabcbaabcbc"
part = "abc"

def removepart(mystr, part):
    pos = mystr.find(part)
    if pos>0:
        mystr = mystr.replace(part,"")
        return removepart(mystr, part)
    else:
        return mystr
    
print(removepart(s, part))