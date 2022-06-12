# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = input()
    B = input()
    A_temp = []
    B_temp = []
    counter = 0
    for _ in range(N):
        if A[_] != B[_]:
            counter += 1
            B_temp.append(B[_])
    print(len(set(B_temp)))
