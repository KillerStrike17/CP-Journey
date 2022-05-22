# cook your dish here
for _ in range(int(input())):
    M, x, y = list(map(int, input().split()))
    N = list(map(int, input().split()))
    N.sort()
    total_houses = x*y
    L = []

    # print(len(count_arr))

    # Approach One
    for i in range(M):
        myrange = max(N[i]-x*y, 1), min(100, N[i]+x*y)
        L.append(myrange)
    # print(L)
    total = L[0][0]-1
    for _ in range(1, M):
        if L[_][0] > L[_-1][1]:
            total += L[_][0] - 1 - L[_-1][1]
            # print(total)

        if _ == (M-1):
            total += 100-L[_][1]
    print(total)

    # ApproachTwo
    count_arr = [1 for _ in range(100)]
    for i in range(M):
        min_val = max(N[i]-x*y, 0)
        max_val = min(99, N[i]+x*y)
        for k in range(min_val, max_val+1):
            count_arr[k] = 0
    print(count_arr.count(1))
    # print(count.count(1))
