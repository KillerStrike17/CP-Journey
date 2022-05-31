# cook your dish here
for _ in range(int(input())):
    X,Y = list(map(int,input().split()))
    if X>Y:
        print("SECOND")
    elif Y>X:
        print("FIRST")
    else:
        print("ANY")
        