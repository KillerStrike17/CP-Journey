mylist = [[1,2,3,4],
          [2,3,4,1],
          [5,6,1,3],
          [2,4,6,8],
          [1,9,9,6]]

key = 5
for i in range(len(mylist[0])):
    # sumval = 0
    for j in range(len(mylist)):
        if mylist[j][i] ==key:
            print(True)
        
print(False)