def isPossible(stalls,k,mid):
    cow_count = 1
    lastPos = stalls[0]
    for _ in range(len(stalls)):
        if stalls[_]-lastPos>=mid:
            cow_count+=1
            if cow_count==k:
                return True
            lastPos = stalls[_]
    return False

def aggressiveCows(stalls, k):
    # Write your code here.
    stalls.sort()
    s = 0
    e = max(stalls) - min(stalls)
    mid = s +(e-s)//2
    ans = -1
    while(s<=e):
        if (isPossible(stalls,k,mid)):
            s = mid +1
            ans = mid
        else:
            e = mid -1        
        mid = s +(e-s)//2
    return ans
    

    pass