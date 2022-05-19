# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    min_val =A[0]
    counter = 1
    for i in range(1,N):
        if min_val<=A[i]:
            continue
        else:
            counter +=1
            min_val = A[i]
    print(counter)