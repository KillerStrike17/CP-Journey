# cook your dish here
for _ in range(int(input())):
    N = int(input())
    if N > 3:
        print(N)
    elif N > 1:
        print(N-1)
    else:
        print(1)
