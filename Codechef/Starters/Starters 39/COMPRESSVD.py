# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    B = A.copy()
    counter = 0
    if N>1:
        for _ in range(N-1):
            if A[_] ==A[_+1]:
                counter += 1
        print(N-counter)
    else:
        print(N)
        
        