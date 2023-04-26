myList = [1,2,3,4,5,9,8,7,6]

maxVal = -9999999
for _ in myList:
    if _>maxVal:
        maxVal = _

print("max Val:",maxVal)