# cook your dish here
for _ in range(int(input())):
    N,X = [int(x) for x in input().split()]
    print(abs(2*N-X+1))