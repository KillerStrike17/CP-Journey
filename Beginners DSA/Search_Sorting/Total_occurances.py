def binary_search_first_occurance(arr,n,k):
    start = 0
    end = n-1
    mid = start + (end-start)//2
    my_list = []
    ans = -1
    while start<=end:
        if k ==arr[mid]:
            ans = mid
            end = mid -1
        elif k>arr[mid] :
            start = mid +1
        elif k<arr[mid]:
            end = mid - 1
        mid = start + (end-start)//2
#     print(my_list)
    return ans

def binary_search_last_occurance(arr,n,k):
    start = 0
    end = n-1
    mid = start + (end-start)//2
    my_list = []
    ans = -1
    while start<=end:
        if k ==arr[mid]:
            ans = mid
            start = mid +1
        elif k>arr[mid] :
            start = mid +1
        elif k<arr[mid]:
            end = mid - 1
        mid = start + (end-start)//2
#     print(my_list)
    return ans


def firstAndLastPosition(arr, n, k):
    # Write your code here
    x = binary_search_last_occurance(arr,n,k)
    if x !=-1:
        return x - binary_search_first_occurance(arr,n,k) +1