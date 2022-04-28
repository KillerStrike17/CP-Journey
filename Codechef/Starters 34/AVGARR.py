# cook your dish here
for _ in range(int(input())):
    i = 1
    N, X = [int(x) for x in input().split()]
    if N & 1:
        for _ in range(N//2):
            print(X-i, X+i, end=" ")
            i += 1
        print(X)
    else:
        for _ in range(N//2):
            print(X-i, X+i, end=" ")
            i += 1
