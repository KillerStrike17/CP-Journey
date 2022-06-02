for _ in range(int(input())):
    N = int(input())
    S = input()
    ones = S.count('1')
    print(ones*(ones+1)//2)
