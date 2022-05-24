# cook your dish here
for _ in range(int(input())):
    check = check_b = 0
    N, X = list(map(int, input().split()))
    S = list(map(int, input().split()))
    for _ in S:
        if _ < X:
            check = 1
        elif _ > X:
            check_b = 1
        else:
            check_b = 1
            check = 1

    if check == 1 and check_b == 1:
        print("YES")
    else:
        print("NO")
