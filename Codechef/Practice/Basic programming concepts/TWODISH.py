# cook your dish here
for _ in range(int(input())):
    N,A, B,C = list(map(int,input().split()))
    if B>=A+C:
        max_food = A+C
    else:
        max_food = B
    if max_food>=N:
        print("YES")
    else:
        print("NO")
        