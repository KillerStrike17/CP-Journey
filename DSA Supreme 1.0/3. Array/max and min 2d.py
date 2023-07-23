mylist = [[1,2,3,4],
          [2,3,4,1],
          [5,6,1,3],
          [2,4,6,8],
          [1,9,9,6]]

maxval = -1
minval = 99

for i in range(len(mylist[0])):
    # sumval = 0
    for j in range(len(mylist)):
        if mylist[j][i]>maxval:
            maxval = mylist[j][i]
        if mylist[j][i]<minval:
            minval = mylist[j][i]
print(maxval,minval)