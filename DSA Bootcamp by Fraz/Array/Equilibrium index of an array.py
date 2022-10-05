def findEquilibrium(a,n):
    # Code here
    left_sum = 0
    right_sum = sum(a)
    for _ in range(n):
        right_sum-=a[_]
        if right_sum==left_sum:
            return _
        left_sum+=a[_]
    return -1
            