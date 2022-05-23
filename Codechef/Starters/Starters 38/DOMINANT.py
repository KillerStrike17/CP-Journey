# cook your dish here
for _ in range(int(input())):
    A, B, C = list(map(int, input().split()))
    if ((A+B) < C or (A+C) < B or (B+C) < A):
        print("YES")
    else:
        print("NO")
