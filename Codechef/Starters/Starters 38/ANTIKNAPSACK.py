# cook your dish here
for _ in range(int(input())):
    p = 1
    X = []
    N, K = list(map(int, input().split()))
    while(K % p == 0):
        p += 1
    for j in range(1, N+1):
        print(p*j, end=" ")
    print()
