# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    check = 0
    ini_value = A[0] % 2
    final_value = A[-1] % 2
    move = [0 for i in range(N)]
    count = count_a = count_b = 0
    if (A[0] % 2 == A[-1] % 2):
        for i in range(1, N):
            if A[i] % 2 == A[-1] % 2:
                count += 1
        print(count)
    else:
        for i in range(1, N):
            if A[0] % 2 != A[i] % 2:
                move[i] = move[i-1] + 1
            else:
                move[i] = move[i-1]
        ans = move[-1]
        for i in range(1, N):
            if (A[i] % 2 == A[0] % 2):
                count_a += 1
                ans = min(ans, count_a + move[-1] - move[i])
        print(ans)
