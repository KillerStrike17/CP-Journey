from collections import Counter


def findDuplicate(arr):
    # Write your code here
    x = Counter(arr)
    for _ in x.keys():
        if x[_] > 1:
            return _
#     n = len(arr)
#     for _ in range(0,n,2):
#         if _ ==n-1:
#             return arr[_]
#         if arr[_]==arr[_+1]:
#             return arr[_]

    pass
