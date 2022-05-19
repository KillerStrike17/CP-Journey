# cook your dish here
for _ in range(int(input())):
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    min_val = S[1] - S[0]
    for _ in range(1,N-1):
        val = S[_+1] - S[_]
        min_val = min(min_val,val)
    print(min_val)