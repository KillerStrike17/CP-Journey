mylist = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(mylist)):
    for j in range(len(mylist[0])):
        print(mylist[i][j],end = " ")
    print("")    
for i in range(len(mylist)):
    for j in range(len(mylist[0])):
        print(mylist[j][i],end = " ")
    print("")