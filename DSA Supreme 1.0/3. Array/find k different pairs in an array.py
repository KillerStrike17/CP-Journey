from collections import defaultdict
arr = [1,1,1,1]

arr.sort()

print(arr)


# 2 Pointer Approach
def twopointer(arr):
    i = 0
    j = 1
    k  = 0
    ans_set = []
    while j<len(arr):
        
        diff = arr[j]-arr[i]
        if diff==k:
            ans_set.append([arr[j],arr[i]])
            i+=1
            j+=1
        elif diff>k:
            i +=1
        else:
            j+=1
        if i == j:
            j+=1
    print(set(tuple(row) for row in ans_set))


# Binary Search

arr = [1,1,3,5,4]
arr.sort()
print(arr)
def bs(arr,start,target):
    # start = start
    # print(arr,start,target)
    end = len(arr)-1
    mid = start + (end -start)//2

    while start<=end:
        print(mid)
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            end = mid -1
        else:
            start = mid + 1
        mid = start + (end -start)//2
    return -1

k=2
ans = []
for _ in range(len(arr)):
    if(bs(arr,_+1,arr[_]+k)!=-1):
        ans.append([arr[_],arr[_]+k])
        print(ans)

print(set(tuple(row) for row in ans))


