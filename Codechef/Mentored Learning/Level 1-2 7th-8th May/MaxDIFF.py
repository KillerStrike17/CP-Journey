# cook your dish here
for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    W = list(map(int, input().split()))
    W.sort()
    if K <= N//2:
        A = W[:K]
        B = W[K:]
        ans = abs(sum(B) - sum(A))
    else:
        W.sort(reverse=True)
        A = W[:K]
        B = W[K:]
        ans = abs(sum(B) - sum(A))
    print(ans)
