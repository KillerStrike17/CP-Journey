# cook your dish here
for _ in range(int(input())):
    X, Y, Z = list(map(int, input().split()))
    print(((X*5)+(Y*10)) // Z)
