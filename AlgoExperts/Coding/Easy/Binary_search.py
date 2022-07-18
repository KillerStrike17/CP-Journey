def binarySearch(array, target):
    s = 0
    e = len(array)-1
    mid = s +(e-s)//2
    ans = -1
    while(s<=e):
        if array[mid] == target:
            return mid
        elif array[mid]>target:
            e = mid-1
        else:
            s = mid+1
        mid = s +(e-s)//2
    return ans
    # Write your code here.
    pass
