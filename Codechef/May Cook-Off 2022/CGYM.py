# cook your dish here
for _ in range(int(input())):
    X, Y, Z = list(map(int, input().split()))
    if X > Z:
        print(0)
    else:
        if X+Y > Z:
            print(1)
        else:
            print(2)
