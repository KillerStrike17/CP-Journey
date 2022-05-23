# cook your dish here
def expiring_bread(T):
    for _ in range(T):
        N, M, K = [int(x) for x in input().split()]
        if N/M > K:
            print("No")
        else:
            print("Yes")


T = int(input())
expiring_bread(T)
