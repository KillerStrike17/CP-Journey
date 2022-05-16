# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A.index(1),A.index(2),A.index(3),A.index(4),A.index(5),A.index(6),A.index(7))+1)