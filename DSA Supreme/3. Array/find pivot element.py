arr = [7,3,4,5,6]

def pivot_element(arr):
    start = 0
    end = len(arr)-1
    mid  = start + (end-start)//2
    
    while(start<=end):
        if mid+1<len(arr) and arr[mid]>arr[mid+1]:
            return mid
        if mid-1> 0 and arr[mid-1]>arr[mid]:
            return mid-1
        if arr[start]>=arr[mid]:
            end = mid-1
        else:
            start = mid+1
        mid  = start + (end-start)//2
    return -1

print(pivot_element(arr))
            