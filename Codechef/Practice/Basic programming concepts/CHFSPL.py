# cook your dish here
for _ in range(int(input())):
    A,B,C = list(map(int,input().split()))
    print(max(A+B,B+C,C+A))