# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    if N & 1:
        print(-1)
    else:

        one = A.count(1)
        neg_one = A.count(-1)
        print(abs(one-neg_one)//2)
