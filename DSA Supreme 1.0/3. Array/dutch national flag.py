myList = [0,1,0,1,1,0,0]

start = 0
end = len(myList) -1
i=0
while start<=end:
    if myList[i] ==0:
        myList[start],myList[i] = myList[i],myList[start]
        i+=1
        start+=1
    elif myList[i] ==1:
        myList[i],myList[end] = myList[end],myList[i]
        # i+=1
        end-=1

print(myList)
