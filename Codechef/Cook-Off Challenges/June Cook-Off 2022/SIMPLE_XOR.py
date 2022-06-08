# cook your dish here
for _ in range(int(input())):
    L, R = list(map(int, input().split()))
    if L % 2 == 0:
        if R >= L+3:
            print(L, L+1, L+2, L+3, sep=' ')
        else:
            print(-1)
    else:
        if R >= L+4:
            print(L+1, L+2, L+3, L+4, sep=' ')
        else:
            print(-1)
