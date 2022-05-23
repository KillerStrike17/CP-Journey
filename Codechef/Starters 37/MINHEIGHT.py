# cook your dish here
for _ in range(int(input())):
    X,H = list(map(int, input().split()))
    if X>=H:
        print("Yes")
    else:
        print("No")
        