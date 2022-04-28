# cook your dish here
T = int(input())

for _ in range(T):
    N, X = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    list_sum = sum(A)
    remaining_blub_value = X*N-list_sum
    if remaining_blub_value >= 0:
        print(remaining_blub_value)
    else:
        print(0)
