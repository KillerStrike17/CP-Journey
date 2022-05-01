# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    check = 0
    for _ in range(1, N-1):
        if abs(A[_]-A[_-1]) == 2*abs(A[_]-A[_+1]):
            continue
        elif 2*abs(A[_]-A[_-1]) == abs(A[_]-A[_+1]):
            continue
        else:
            print("No")

            check = 1
            break
    if check == 0:
        print("Yes")
