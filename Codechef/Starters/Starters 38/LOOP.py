# cook your dish here
for _ in range(int(input())):
    A, B, M = list(map(int, input().split()))
    val1 = abs(B-A)
    val2 = abs(M-B) + A
    print(min(val1, val2))
