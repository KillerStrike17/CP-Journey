from collections import defaultdict
mylist = [1,2,3,4,2,6]
mydict = defaultdict(int)

for _ in mylist:
    mydict[_] +=1

number = 1
for _ in mydict:
    if _ != number:
        print(number)
        break
    number +=1