mylist = [[1,2,3,4,5,6],
          [7,8,9,10,11,12],
          [13,14,15,16,17,18],
          [19,20,21,22,23,24],
          [25,26,27,28,29,30]]
m = len(mylist)
n = len(mylist[0])
startRow =startCol = 0
endRow = m - 1
endCol = n - 1
total_elements = m*n
count = 0
# print(m,n)
while count<total_elements:
    for _ in range(startCol,endCol):
            print(mylist[startRow][_], end = " ")
            count+=1
    
    for _ in range(startRow, endRow):
            print(mylist[_][endCol], end = " ")
            count+=1
    
    for _ in range(endCol, startCol, -1):
            print(mylist[endRow][_], end = " ")
            count+=1
    
    for _ in range(endRow, startRow, -1):
            print(mylist[_][startCol], end = " ")
            count+=1
    # break
        
    
    startRow +=1
    endCol -=1
    endRow -=1
    startCol +=1
    
    