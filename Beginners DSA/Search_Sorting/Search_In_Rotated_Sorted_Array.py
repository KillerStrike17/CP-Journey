def pivot_element(arr,n):
    s = 0
    e = n-1
    mid = s+(e-s)//2
    while s<e:
        if arr[mid]>=arr[0]:
            s = mid+1
        else:
            e = mid
        mid = s+(e-s)//2
    return s

def bs(arr,n,k,s,e):
    s = s
    e = e
    mid = s+(e-s)//2
    while(s<=e):
        if arr[mid] ==k:
            return mid
        elif k>arr[mid]:
            s = mid +1
        elif k<arr[mid]:
            e = mid-1
        mid = s+(e-s)//2
    return -1
#     pass


def findPosition(arr, n, k):

	# Write your code here
    pivot = pivot_element(arr,n)
#     print(pivot)
#     sys.exit(0)
    if k>=arr[pivot] and k<=arr[-1]:
        return bs(arr,n,k,pivot,n-1)
    else:
        return bs(arr,n,k,0,pivot-1)