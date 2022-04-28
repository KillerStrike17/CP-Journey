# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    check = 0
    for _ in range(N-1):
        if A[_] > A[_+1]:
            temp = A[_]
            A[_] = A[_+1]
            A[_+1] = temp
            break
    if A == sorted(A):
        print("YES")
    else:
        print("NO")
