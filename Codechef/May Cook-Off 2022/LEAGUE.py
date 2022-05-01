# cook your dish here
import math
for _ in range(int(input())):
    N = int(input())
    max_win = (N-1)*3
    second_max_win = math.ceil((N-2)/2)*3
    print(max_win-second_max_win)
