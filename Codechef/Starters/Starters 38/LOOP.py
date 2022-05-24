# cook your dish here
for _ in range(int(input())):
    A, B, M = list(map(int, input().split()))
    val1 = abs(A-B)
    # val2 = abs(M-B) + A
    val2 = M-abs(A-B)
    print(min(val1, val2))
