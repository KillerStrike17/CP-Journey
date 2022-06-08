# cook your dish here
for _ in range(int(input())):
    X,Y = list(map(int,input().split()))
    if Y<=X+200 and Y>=X:
        print("YES")
    else:
        print("NO")
        