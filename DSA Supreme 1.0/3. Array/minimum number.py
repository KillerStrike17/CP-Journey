myList = [1,2,3,4,5,9,8,7,6]

minVal = 9999999
for _ in myList:
    if _<minVal:
        minVal = _

print("min Val:",minVal)