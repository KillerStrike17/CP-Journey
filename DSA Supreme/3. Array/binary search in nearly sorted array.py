arr = [10,3,40,20,50,80,70]
target = 700
def bs(arr, target):
    start = 0
    end = len(arr)-1
    mid = start + (end-start)//2

    while start<=end:
        if target == arr[mid]:
            return mid
        
        if mid-1<=start and target == arr[mid-1]:
            return mid-1
        if mid+1<=end and target == arr[mid+1]:
            return mid+1
        if arr[mid]>target:
            end  =mid-2
        else:
            start = mid+2
        mid = start + (end-start)//2
    return -1

print(bs(arr, target))