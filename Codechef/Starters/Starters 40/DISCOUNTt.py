# cook your dish here
for _ in range(int(input())):
    N,X,Y = list(map(int,input().split()))
    A = list(map(int,input().split()))
    val = sum(A)
    new_val = 0
    for _ in A:
        new_val += max(0,_-Y)
    new_val += X
    if new_val<val:
        print("COUPON")
    else:
        print("NO COUPON")
        
        