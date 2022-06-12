# cook your dish here
for _ in range(int(input())):
    A, B = list(map(int, input().split()))
    if A & 1 and B & 1 or A % 2 == 0 and B % 2 == 0:
        print("YES")
    else:
        print("NO")
