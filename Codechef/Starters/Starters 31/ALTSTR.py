# cook your dish here
for _ in range(int(input())):
    N = int(input())
    S = input()
    ones = S.count('1')
    zeros = S.count('0')
    if ones>zeros:
        print(2*zeros + 1)
    elif zeros>ones: 
        print(2*ones +1 )
    else:
        print(2*ones)