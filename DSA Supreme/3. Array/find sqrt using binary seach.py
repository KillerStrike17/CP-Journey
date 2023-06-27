import numpy as np
def sqrt(n):
    start = 0
    end = n
    mid = start + (end-start)//2
    ans = -1
    while start<=end:
        if (mid*mid ==  n):
            return mid
        elif (mid*mid >  n):
            end = mid -1
        else:
            ans = mid
            start = mid +1
        
        
        mid = start + (end-start)//2
    return ans
n =10
ans = sqrt(n)
# print(ans)
finalans = ans
p = 4
step = 0.1
for i in range(p):
    j = finalans
    while j*j<=n:
        finalans = j
        j +=step
    step = step/10
print(finalans)
    