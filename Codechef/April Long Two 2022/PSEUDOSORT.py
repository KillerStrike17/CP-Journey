# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    check = 0
    for _ in range(N-1):
        if A[_]>A[_+1]:
            check+=1
        if _<N-2 and A[_]>A[_+2]:
            check +=1
    if check <= 1:
        print("Yes")
    else:
        print("No")
        