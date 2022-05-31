# cook your dish here
import math
for _ in range(int(input())):
    X,Y = list(map(int,input().split()))
    print(math.ceil((Y-X)/8))