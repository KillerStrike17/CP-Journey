# cook your dish here
pos = 0
for _ in range(int(input())):
    N = int(input())
    
    # if pos>-1:
    #     pos -= N
    # else:
    #     pos += N
    # print(pos)
    if N&1:
        print(-(N+1)//2)
    else:
        print(N//2)