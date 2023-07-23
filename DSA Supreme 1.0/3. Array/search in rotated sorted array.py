arr = [7,1]
target = 1

def find_pivot(arr):
    start = 0
    end = len(arr)-1
    mid = start + (end - start)//2
    
    while start<=end:
        if arr[mid]>arr[mid+1]:
            return mid
        if arr[mid-1]>arr[mid]:
            return mid-1
        if arr[start] >arr[mid]:
            end = mid -1
        else:
            start = mid +1 
        mid = start + (end - start)//2
    return -1

def bs(arr, target, start, end):
    # print(target, start, end)
    start = start
    end = end
    mid = start + (end-start)//2
    while start<=end:
        if arr[mid] == target:
            return mid
        if arr[mid]>target:
            end = mid -1
        else:
            start = mid+1
        
        mid = start + (end-start)//2
    return -1

index = find_pivot(arr)
print(index)

if target>=arr[0] and target<=arr[index]:
    print(bs(arr, target, 0, index))
elif target>=arr[index+1] and target<=arr[len(arr)-1]:
    print(bs(arr, target, index+1, len(arr)-1))
# else:
#     print(index)
    
    
