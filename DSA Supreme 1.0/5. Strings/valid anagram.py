from collections import defaultdict
s = "anagram"
t = "aaagnrma"

# print(sorted(s) ==sorted(t))

sdict = defaultdict(lambda:0)
tdict = defaultdict(lambda:0)

for _ in s:
    sdict[_] +=1

keys = sdict.keys()
check = True    
for _ in t:
    if _ in sdict and sdict[_]>0:
        sdict[_]-=1
    
    else:
        check = False
        break
if check != False:
    for _ in sdict.values():
        if _!=0:
            check = False

print(check)