# cook your dish here
for _ in range(int(input())):
    N, X = list(map(int,input().split()))
    space,imdb=[],[]
    for _ in range(N):
        S,R = list(map(int,input().split()))
        if X>=S:
            space.append(S)
            imdb.append(R)
    print(max(imdb))
    # print(space)
    # print(imdb)