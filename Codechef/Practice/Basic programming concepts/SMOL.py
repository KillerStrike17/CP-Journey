# cook your dish here
for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    # while N>=0:
        # N = N - K
    if K==0:
        print(N)
    else:
        print(N%K)