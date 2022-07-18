# cook your dish here
def isPossible(arr,N,M,mid):
    wood_tot = 0
    # lastPos = arr[0]
    for _ in range(N):
        if arr[_]>mid:
            wood_tot +=arr[_]-mid
    if wood_tot >=M:
        return True
            # lastPos ==arr[_]             
    return False


for _ in range(int(input())):
    N,M= list(map(int,input().split()))
    arr= list(map(int,input().split()))
    s = 0
    e  =max(arr)
    mid = s+(e-s)//2
    ans =0
    while(s<=e):
        if (isPossible(arr,N,M,mid)):
            s = mid+1
            ans = mid
        else:
            e = mid-1
        mid = s+(e-s)//2
    print(ans)