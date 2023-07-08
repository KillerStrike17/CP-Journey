n = 5
k = 3
stalls = [1,2,4,8,9]
def isPositionPossible(stalls, n,k, mid):
    distance = 0
    c = 1
    for _ in range(n):
        if stalls[_]>mid:
            return False
        if distance + stalls[_]>mid:
            distance = stalls[_]
            c+=1
            if c>k:
                return False
        else:
            distance +=mid
    return True
            


def agg_cows(stalls, n, k):
    
    start = 0
    end = stalls[-1] - stalls[0]
    ans = -1
    while start<=end:
        mid =start + (end- start)//2
        print(start, mid, end)
        if isPositionPossible(stalls, n,k, mid):
            start +=1
            ans = mid
        else:
            end = mid -1
    return ans

print(agg_cows(stalls, n, k))