# cook your dish here

X, Y = [int(x) for x in input().split()]
d = {}
for _ in range(2, X+1):
    while(X % _ == 0):
        X /= _
        if _ in d.keys():
            d[_] += 1
        else:
            d[_] = 1

for _ in range(2, Y+1):
    while(Y % _ == 0):
        Y /= _
        # print(_)
        # counter += 1
        if _ in d.keys():
            d[_] += 1
        else:
            d[_] = 1

ans = 1
for _ in d.values():
    ans *= (_+1)
print(ans)
