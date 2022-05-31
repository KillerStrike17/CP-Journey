# cook your dish here
for _ in range(int(input())):
    X,Y = list(map(int,input().split()))
    A = 500-X*2 + 1000-(X+Y)*4
    B = 500-(X+Y)*2 + 1000-(Y)*4
    # print(A,B)
    print(max(A,B))