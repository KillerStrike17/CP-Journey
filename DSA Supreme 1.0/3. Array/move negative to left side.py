mylist = [1,2,3,-4,-5,6]

start = 0
end = len(mylist)-1

while start<end:
    if mylist[start]<0:
        start +=1
    elif mylist[end]>0:
        end -=1
    else:
        mylist[start],mylist[end] = mylist[end],mylist[start]

print(mylist)
    
        