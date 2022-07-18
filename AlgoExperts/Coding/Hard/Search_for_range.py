def start_bs(array,target):
    s = 0
    e = len(array)-1
    mid = s +(e-s)//2
    ans = -1
    while(s<=e):
        if array[mid] ==target:
            e = mid-1
            ans = mid
        elif array[mid]>target:
            e = mid-1
        else:
            s = mid+1
        mid = s +(e-s)//2
    return ans

def end_bs(array,target):
    s = 0
    e = len(array)-1
    mid = s +(e-s)//2
    ans = -1
    while(s<=e):
        if array[mid] ==target:
            s = mid+1
            ans = mid
        elif array[mid]>target:
            e = mid-1
        else:
            s = mid+1
        mid = s +(e-s)//2
    return ans
    # Write your code here.
    pass


def searchForRange(array, target):
    # Write your code here.
    # print(array,target)
    return [start_bs(array, target),end_bs(array, target)]
    pass
