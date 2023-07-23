mylist = [0,0,2,1,1,2,0]

l = m =0
h = len(mylist) -1

while m<h:
    if mylist[m] ==0:
        mylist[l],mylist[m] = mylist[m],mylist[l]
        m +=1
        l +=1
    elif mylist[m] ==1:
        m+=1
    
    elif mylist[m] ==2:
        mylist[m],mylist[h] = mylist[h],mylist[m]
        h -=1

print(mylist)