# cook your dish here
for _ in range(int(input())):
    N,S = list(map(int, input().split()))
    if N>=S:
        print(S)
    else:
        val = S-N
        print(abs(val-N))
        