def isPossible(boards,k,mid):
    painterCount = 1
    area = 0
    for _ in range(len(boards)):
        if (area+boards[_])<=mid:
            area+=boards[_]
        else:
            painterCount +=1
            if painterCount>k or boards[_]>mid:
                return False
            area = 0
            area+=boards[_]
    return True           

def findLargestMinDistance(boards:list, k:int):
    # Write your code here
    # Return an integer
    s = 0
    ans = -1
    e = sum(boards)
    mid = s+(e-s)//2
    while(s<=e):
#         print(mid)
        if (isPossible(boards, k,mid)):
            e = mid -1
            ans = mid
        else:
            s = mid+1
        mid = s+(e-s)//2
    return ans
            
    pass