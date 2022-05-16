# cook your dish here
for _ in range(int(input())):
    total_time = 0
    N,P,X,Y = list(map(int,input().split()))
    A = list(map(int,input().split()))
    for _ in range(N):
        if P==_:
            break
        else:
            if A[_]==0:
                total_time  += X
            else:
                total_time  += Y
    print(total_time)