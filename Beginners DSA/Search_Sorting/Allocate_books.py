def isPossible(arr,n,m,mid):
    dayCount = 1
    timesum = 0
    for _ in range(m):
#         print(dayCount,'   ', timesum, '   ', mid,'   ',arr[_])
        if((timesum+arr[_])<=mid):
#             print(dayCount,'   ', timesum, '   ', mid,'   ',arr[_])
            timesum +=arr[_]
        else:
            
            dayCount +=1
#             print(dayCount,'   ', timesum, '   ', mid,'   ',arr[_])
            if dayCount>n or arr[_]>mid:
#                 print('in elseif')
                return False
            timesum = 0
            timesum +=arr[_]
    return True            

def ayushGivesNinjatest(n, m, time):
    s = 0
    e= sum(time)
    mid = s+ (e-s)//2
    ans = -1
    
    while(s<=e):
#         print('ans',ans,'mid',mid)
        if (isPossible(time,n,m,mid)):
#             print('In if')
            ans = mid
            e = mid-1
        else:
#             print('In else')
            s = mid+1
        mid = s+ (e-s)//2
    return ans       
            
    pass