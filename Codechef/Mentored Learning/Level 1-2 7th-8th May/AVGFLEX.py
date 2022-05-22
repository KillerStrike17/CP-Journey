# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    counter = N//2
    temp = A[counter]
    if N&1:
        for _ in range(0,N//2 +1):
            if A[_] == temp:
                counter += 1
    else:
        for _ in range(0,N//2):
            if A[_] == temp:
                counter += 1
    print(counter)
        