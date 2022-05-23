# cook your dish here
for _ in range(int(input())):
    X,Y = list(map(int, input().split()))
    if Y*10 >X*100:
        print("Disposable")
    else:
        print("Cloth")
    