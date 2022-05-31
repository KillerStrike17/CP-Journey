# cook your dish here
for _ in range(int(input())):
    X,Y = list(map(int,input().split()))
    if X>= Y*30:
        print("YES")
    else:
        print("NO")