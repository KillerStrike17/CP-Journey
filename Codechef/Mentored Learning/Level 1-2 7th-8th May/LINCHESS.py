# cook your dish here
for _ in range(int(input())):
    N,K = list(map(int,input().split()))
    P = list(map(int,input().split()))
    P.sort()
    val = -1
    for _ in P[::-1]:
        if K%_ ==0:
            val = _
            break
    print(val)
        