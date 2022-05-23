# cook your dish here
for _ in range(int(input())):
    N, X, Y = list(map(int, input().split()))
    S = input()
    zeros = S.count('0')
    ones = S.count('1')

    if ones > 0 and zeros > 0:
        if X > Y:
            print(Y)
        else:
            print(X)
    else:
        print(0)
