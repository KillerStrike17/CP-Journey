# cook your dish here
for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if K >= N-1:
        K = N-1

    for _ in range(K):
        A.pop()
    print(min(A))
