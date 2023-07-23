def check_sort(arr, index, n):
    if index>=n:
        return True
    if arr[index]<arr[index-1]:
        return False
    return check_sort(arr, index+1, n)


print(check_sort([1,2,3,4,5,6,7,8,0],1,9))

    
