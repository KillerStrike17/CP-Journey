# cook your dish here
for _ in range(int(input())):
    X,Y= list(map(int,input().split()))
    if X ==1:
        print(0)
    else:
        print((X-1) *(2*Y - X))