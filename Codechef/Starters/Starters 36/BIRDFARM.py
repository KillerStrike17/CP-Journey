# cook your dish here
for _ in range(int(input())):
    X, Y, Z = [int(x) for x in input().split()]
    if Z % X == 0 and Z % Y == 0:
        print("ANY")
    elif Z % X == 0:
        print("CHICKEN")
    elif Z % Y == 0:
        print("DUCK")
    else:
        print("NONE")
