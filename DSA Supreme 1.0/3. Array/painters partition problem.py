arr = [5,10,30,20,15]

n = 5
k =3

def possibleJob(arr, n, k, mid):
    print(arr, n,k, mid)
    painterTime = 0
    c = 1
    for i in range(n):
        if arr[i]>mid:
            return False
        if (painterTime + arr[i])>mid:
            painterTime = arr[i]
            c +=1
            if c>k:
                return False
        else:
            painterTime += arr[i]
    return True


def allocateJob(arr, n, k):
    start = 0
    end = sum(arr)
    
    ans = -1    
    while start<=end:
        mid = start + (end-start)//2
        print(start, end, mid)
        if possibleJob(arr, n, k, mid):
            ans = mid
            end = mid-1
        else:
            start =mid +1
        # mid = start + (end-start)//2
    return ans

print(allocateJob(arr, n, k))