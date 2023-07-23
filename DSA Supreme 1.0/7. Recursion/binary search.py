def bs(start, end, target, arr):
    mid = (start+end)//2
    # print(start, end)
    if start>end:
        return -1
    if arr[mid] == target:
        return mid
    if arr[mid]>target:
        return bs(start, mid-1, target, arr)
    else:
        return bs(mid+1, end, target, arr)


arr = [1,2,3,4,5,6,7,8,9]
target = 9
print(bs(0,len(arr)-1,target,arr))

