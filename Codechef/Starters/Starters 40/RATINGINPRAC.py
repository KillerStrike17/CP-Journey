# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    B = A.copy()
    A.sort()
    if B == A:
        print("YES")
    else:
        print("NO")