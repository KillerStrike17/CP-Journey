# cook your dish here
for _ in range(int(input())):
    X, Y = list(map(int, input().split()))
    if Y >= X:
        print(0)
    else:
        print(X-Y)
