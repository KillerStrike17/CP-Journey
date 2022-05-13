# cook your dish here
import math
for _ in range(int(input())):
    U, V, A, S = list(map(int,input().split()))
    ans= U*U - 2*A*S
    if ans<0:
        print("Yes")
    else:
        ans = math.sqrt(ans)
        if V>=ans:
            print("Yes")
        else:
            print("No")
    