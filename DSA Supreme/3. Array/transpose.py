mylist = [[1,2,3,4],
          [2,3,4,1],
          [5,6,1,3],
          [2,4,6,8]]
temp =[]
print(mylist)
for i in range(len(mylist[0])):
    # sumval = 0
    rowtemp = []
    for j in range(len(mylist)):
        rowtemp.append(mylist[j][i])
    temp.append(rowtemp)

print(temp)