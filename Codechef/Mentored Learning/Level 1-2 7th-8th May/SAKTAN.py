# cook your dish here
for _ in range(int(input())):
    N, M, Q = list(map(int, input().split()))
    row = [0]*N
    col = [0]*M
    for k in range(Q):
        X, Y = list(map(int, input().split()))
        row[X-1] += 1
        col[Y-1] += 1
    counter = 0
    od_r = len([x for x in row if x & 1])
    ev_r = len([x for x in row if x % 2 == 0])
    od_c = len([x for x in col if x & 1])
    ev_c = len([x for x in col if x % 2 == 0])
    print(od_r*ev_c + ev_r*od_c)
