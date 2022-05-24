# cook your dish here
N, D = list(map(int, input().split()))
L = []
for _ in range(N):
    L.append(int(input()))
L.sort()
i = counter = 0
while(i < N-1):
    # print(i)
    if L[i+1]-L[i] <= D:
        counter += 1
        i += 2
    else:
        i += 1
print(counter)
