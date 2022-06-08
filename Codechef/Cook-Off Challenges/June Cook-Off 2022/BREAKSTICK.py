# cook your dish here
for _ in range(int(input())):
    N, X = list(map(int, input().split()))
    val = N-X
    if ((X % 2 == 0 and val % 2 == 0) or (X % 2 != 0 and val % 2 != 0) or (X % 2 != 0 and val % 2 == 0)):
        print("YES")
    elif (X % 2 == 0 and val % 2 != 0):
        print("NO")
