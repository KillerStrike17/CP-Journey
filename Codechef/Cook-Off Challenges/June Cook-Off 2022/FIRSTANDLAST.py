# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    max_value = A[0] + A[-1]
    for _ in range(N-1):
        if A[_] + A[_+1] > max_value:
            max_value = A[_] + A[_+1]
    print(max_value)
