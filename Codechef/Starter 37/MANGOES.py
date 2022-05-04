# cook your dish here
for _ in range(int(input())):
    X,Y,Z = list(map(int,input().split()))
    mango_max_weight = Z-Y
    max_mangoes = mango_max_weight//X
    print(max_mangoes)