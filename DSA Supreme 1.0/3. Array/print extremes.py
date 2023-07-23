myList = [1,2,3,4,5,6,7,8]
n = len(myList)

for _ in range(n//2):
    print(myList[_],myList[n-_-1])
if n%2!=0:
    print(myList[n//2])

