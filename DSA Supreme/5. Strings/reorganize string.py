from collections import defaultdict
import math
mystr = "aaabbbbbbccdde"
mystrlist = list(mystr)

mydict = defaultdict(lambda:0)

for _ in mystr:
    mydict[_]+=1

maxVal = -1
maxChar = ""
for key, value in mydict.items():
    if value>maxVal:
        maxChar = key
        maxVal = value

print(maxChar)
print(maxVal)

if maxVal>(math.ceil(len(mystr)/2)):
    # print(math.ceil(len(mystr)/2))
    print("here")
else:
    index = 0
    print(mystrlist)
    while mydict[maxChar]>0:
        mystrlist[index] = maxChar
        mydict[maxChar] -=1
        index +=2
    print(mystrlist)
    print(mydict)
    print(index)
    for key, value in mydict.items():
        while(value>0):
            if index >=len(mystr):
                index = 1
            mystrlist[index] = key
            index +=2
            value-=1
            # print(mystrlist)
            
    print("".join(mystrlist))
        