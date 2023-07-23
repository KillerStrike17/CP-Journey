myList = [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1]
countZero = countFirst =0
for _ in myList:
    if _ ==0:
        countZero += 1
    else:
        countFirst += 1

print("Zero Count:",countZero)
print("One Count:",countFirst)