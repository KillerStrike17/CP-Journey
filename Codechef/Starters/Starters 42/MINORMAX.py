# cook your dish here
for _ in range(int(input())):
    N = int(input())
    B = list(map(int, input().split()))
    min_val = max_val = B[0]
    # max_val = max(B)
    val = "YES"
    for _ in B:
        if _ >= max_val:
            max_val = _
        elif _ <= min_val:
            min_val = _
        else:
            val = "NO"
            break
    print(val)
