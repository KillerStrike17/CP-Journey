from collections import defaultdict
mylist = [1,5,3,4,3,5,6]

mydict=defaultdict(int)
for _ in mylist:
    mydict[_] +=1
print(mydict)
for _ in range(len(mylist)):
    if mydict[mylist[_]] >1:
        print(_)
        break

