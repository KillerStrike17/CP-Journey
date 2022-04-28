# cook your dish here
for _ in range(int(input())):
    X, Y = [int(x) for x in input().split()]
    if X > Y:
        print("A")
    else:
        print("B")
