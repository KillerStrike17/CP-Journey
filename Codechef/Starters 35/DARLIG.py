# cook your dish here
for _ in range(int(input())):
    N, K = list(map(int, input().split()))
    if K == 0:
        if N % 4 == 0:
            print("Off")
        else:
            print("On")
    else:
        if N % 4 == 0:
            print("On")
        else:
            print("Ambiguous")
