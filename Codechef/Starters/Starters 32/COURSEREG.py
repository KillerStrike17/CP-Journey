# cook your dish here
for _ in range(int(input())):
    N, M, K = list(map(int, input().split()))
    if N+K <= M:
        print("YES")
    else:
        print("NO")
