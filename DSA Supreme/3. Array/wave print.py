mylist = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

rows =  len(mylist)
cols = len(mylist[0])

for i in range(cols):
    if i&1 ==0:
        for j in range(rows):
            print(mylist[j][i], end = " ")
    else:
        for j in range(rows-1,-1,-1):
            print(mylist[j][i], end = " ")
    # print("")
        

