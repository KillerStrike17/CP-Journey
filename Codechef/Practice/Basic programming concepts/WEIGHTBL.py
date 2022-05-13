# cook your dish here
for _ in range(int(input())):
    w1,w2,x1,x2,M = list(map(int, input().split()))
    min_inc = w1+ x1*M
    max_inc = w1+x2*M
    if w2>=min_inc and w2<=max_inc:
        print(1)
    else:
        print(0)