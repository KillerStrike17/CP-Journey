# cook your dish here
for _ in range(int(input())):
    N = int(input())
    if N == 2:
        print(0)
    if N & 1:
        print(((N-1)//2 * (N+1)//2) - 1)
    else:
        if (((N//2)+1) % 2 == 0):
            print(((N//2)-2) * ((N//2) + 2) - 1)
        else:
            print((N//2 - 1) * ((N//2) + 1) - 1)
    # N,M,Q = list(map(int,input().split()))
    # for _ in range(Q):
    #     X,Y =
