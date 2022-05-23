# cook your dish here
for _ in range(int(input())):
    X,Y = list(map(int, input().split()))
    double_room = Y*2
    triple_room = X*3
    if triple_room<=double_room:
        print(triple_room)
    else:
        print(double_room)