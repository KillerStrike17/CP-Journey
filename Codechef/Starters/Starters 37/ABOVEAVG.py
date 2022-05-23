# cook your dish here
import math
for _ in range(int(input())):
    N,M,X = list(map(int, input().split()))
    if M==X:
        print(0)
    else:
        min_mark = X+1
        # new_total = min_mark*N
        # diff = new_total-N*X
        print(N-math.ceil(N/min_mark))