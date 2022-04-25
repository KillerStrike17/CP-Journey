# cook your dish here
for _ in range(int(input())):
    X,Y,D = [int(x) for x in input().split()]
    if abs(X-Y)<=D:
        print("YES")
    else:
        print("NO")
        