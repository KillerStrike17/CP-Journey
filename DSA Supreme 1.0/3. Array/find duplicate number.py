from collections import defaultdict
mylist = [1,2,3,4,2]
mydict = defaultdict(int)

for _ in mylist:
    mydict[_] +=1

for _ in mydict:
    if mydict[_] >1:
        print(_)