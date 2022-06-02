# cook your dish here
for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    if N & 1 and K == 0:
        print("No")
    else:
        print("Yes")
