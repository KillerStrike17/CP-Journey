# cook your dish here
for _ in range(int(input())):
    N = int(input())
    S = list(map(int, input().split()))
    D = list(map(int, input().split()))
    counter = 0
    for _ in range(N):
        if S[_] ==D[_]:
            counter += 1
    print(counter)