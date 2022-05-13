# cook your dish here
for _ in range(int(input())):
    D,L,R = list(map(int,input().split()))
    if D>=L and D<=R:
        print('Take second dose now')
    elif D<L:
        print("Too Early")
    elif D>R:
        print('Too Late')