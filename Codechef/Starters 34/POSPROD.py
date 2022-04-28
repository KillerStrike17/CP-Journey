# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    X = [i for i in A if i != 0]
    pos = len([i for i in X if i > 0])
    neg = len([i for i in X if i < 0])
    print(int(pos*(pos-1)/2) + int(neg*(neg-1)/2))
