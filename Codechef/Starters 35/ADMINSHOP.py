# cook your dish here
import math
for _ in range(int(input())):
    N, X = list(map(int, input().split()))
    A = list(map(int, input().split()))
    min_val = min(A)
    # print(min_val)
    # print(min_val/X)
    ceil_val = math.ceil(X/min_val)
    if ceil_val < N:
        print(N)
    else:
        print(ceil_val)
    # print(math.ceil(min_val/X))
