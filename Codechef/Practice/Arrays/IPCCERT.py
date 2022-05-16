# cook your dish here
counter = 0
N, M, K = list(map(int, input().split()))
for _ in range(N):
    T = list(map(int, input().split()))
    Q = T[-1]
    T = T[:-1]
    # print(Q)
    # print(T)
    mins = sum(T)
    if mins>=M and Q<=10:
        counter +=1
print(counter)