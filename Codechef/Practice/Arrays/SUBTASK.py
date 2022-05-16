# cook your dish here
for _ in range(int(input())):
    N,M,K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    if A.count(1)==N:
        print(100)
    elif A[:M].count(1)==M:
        print(K)
    else:
        print(0)