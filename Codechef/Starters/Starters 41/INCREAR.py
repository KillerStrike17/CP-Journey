# cook your dish here
import math
for _ in range(int(input())):
    X, Y = list(map(int, input().split()))
    if Y > X:
        print(Y-X)
    elif X > Y:
        if ((X & 1 and Y & 1) or (X % 2 == 0 and Y % 2 == 0)):
            print(math.ceil((X-Y)/2))
        else:
            print(math.ceil((X-Y)/2) + 1)
    else:
        print(0)
