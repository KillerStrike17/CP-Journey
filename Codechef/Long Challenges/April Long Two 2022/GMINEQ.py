# cook your dish here
for _ in range(int(input())):
    N = int(input())
    S = [int(x) for x in input().split()]
    ones = S.count(1)
    neg = S.count(-1)
    if abs(ones-neg) < 2:
        print("YES")
    elif abs(ones-neg) == 2:
        if neg % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
