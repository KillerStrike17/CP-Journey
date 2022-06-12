# cook your dish here
import math
for _ in range(int(input())):
    N, X = list(map(int, input().split()))
    val = math.ceil(N/6)
    print(val*X)
