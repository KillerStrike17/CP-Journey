# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    check = [0 for _ in range(32)]
    for _ in range(N):
        check[A[_].bit_length()] += 1
    # print(check)
    res = int(sum([n*(n-1)/2 for n in check]))
    print(res)