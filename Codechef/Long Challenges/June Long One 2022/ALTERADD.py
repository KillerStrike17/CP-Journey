# cook your dish here
for _ in range(int(input())):
    A, B = list(map(int, input().split()))
    val = B-A
    if val % 3 == 0 or val % 3 == 1:
        print("YES")
    else:
        print("NO")
