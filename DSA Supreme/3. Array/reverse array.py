myList = [1,2,3,4,5,6,7]
n = len(myList)
for _ in range(n//2):
    myList[_],myList[n-_-1] = myList[n-_-1],myList[_]
print(myList)