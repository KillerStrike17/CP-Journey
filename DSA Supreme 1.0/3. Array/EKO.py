N = 4
M = 7
arr = [20,15,10,17]

def cut(arr, M, mid):
    woodCollected = 0
    for _ in range(len(arr)):
        if arr[_]>mid:
            woodCollected += arr[_] - mid

    return woodCollected>=M
def cutTrees(arr, N,M):
    start = 0
    end = max(arr)
    ans = -1
    while start<=end:
        mid = start + (end - start)//2
        if cut(arr, M, mid):
            ans = mid
            start =mid + 1
        else:
            
            end = mid -1
        
    return ans

print(cutTrees(arr, N,M))
