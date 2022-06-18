# cook your dish here
for _ in range(int(input())):
    K, X = list(map(int, input().split()))
    total_days = K*7
    print(total_days-X)
