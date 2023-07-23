arr =[12, 34,67,90]
n = len(arr)
m =2

def checkSolution(arr, n, m, mid):
    pageSum = 0
    c = 1
    for i in range(n):
        if arr[i]>mid:
            return False
        if (pageSum+arr[i])>mid:
            c+=1
            pageSum = arr[i]
            if c>m:
                return False
        else:
            pageSum +=arr[i]
    
    return True

def findpages(arr, n, m):
    if m>n:
        return -1
    start = 0
    end = sum(arr)
    ans = -1
    mid = (start + end)//2
    while start<=end:
        if checkSolution(arr, n, m, mid):
            ans = mid
            end = mid -1
        else:
            start +=1
        mid = (start + end)//2
    return ans

print(findpages(arr, n, m))