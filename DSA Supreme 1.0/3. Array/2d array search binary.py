arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
def matrixsearch(arr,target):
    start = 0
    rows = len(arr)
    cols = len(arr[0])
    end = rows*cols - 1
    mid = start + (end-start)//2
    while start<=end:
        rowIndex = mid//cols
        colIndex = mid%cols
        val = arr[rowIndex][colIndex]
        if val == target:
            return True
        elif val>target:
            end = mid-1
        else:
            start = mid+1
        mid = start + (end-start)//2
    return False

print(matrixsearch(arr,144))
