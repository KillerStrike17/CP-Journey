# cook your dish here
for _ in range(int(input())):
    N, X = list(map(int, input().split()))
    if X % N == 0:
        print("YES")
    else:
        print("NO")
