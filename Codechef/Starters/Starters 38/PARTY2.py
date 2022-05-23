# cook your dish here
for _ in range(int(input())):
    N, X, K = list(map(int, input().split()))
    if N*X <= K:
        print("YES")
    else:
        print("NO")
