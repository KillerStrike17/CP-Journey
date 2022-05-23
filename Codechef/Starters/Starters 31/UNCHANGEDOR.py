import math

def Log2(x):
    return int(math.log10(x)/math.log10(2))
# cook your dish here

ans = 0
for _ in range(int(input())):
    N = int(input())
    val = Log2(N)
    
    print(N-val-1)
    # print()
    # if val<3:
        
    #     val = 2**(N-2)
    #     # print(val)
    #     # print(val-1)
    #     #  print((2^(N-1))-1)
    # else:
    #     print(ans)
    # print(N-1)
    # print()
    # print((2^(N-1))-1)