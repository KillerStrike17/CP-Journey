def binarySearch(array, target,s,e):
    s = s
    e = e
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

def shiftedBinarySearch(array, target):
    # Write your code here.
    s = 0
    e = len(array)-1
    m = s+(e-s)//2
    while(s<e):
        # print(s,e,m)
        if (array[m]>=array[0]):
            s = m+1
        else:
            e = m
        m = s+(e-s)//2
    if target>=array[m] and target<array[0]:
        return binarySearch(array, target,m,len(array)-1)
    else:
        return binarySearch(array, target,0,m)
    # print(array,m)
    # binarySearch(array, target,s,e)
    pass
