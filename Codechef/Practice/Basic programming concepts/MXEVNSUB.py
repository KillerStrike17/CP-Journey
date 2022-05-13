# cook your dish here
for _ in range(int(input())):
    N = int(input())
    if N%2==0:
        val = N//2
        if val%2==0:
            print(N)
        else:
            print(N-1)
    else:
        val = N//2
        if val%2==0:
            print(N-1)
        else:
            print(N)