# cook your dish here
for _ in range(int(input())):
    a,b,c,d,K = list(map(int, input().split()))
    total_moves = abs(a-c) + abs(b-d)
    if K==total_moves:
        print("Yes")
    elif K>total_moves:
        ans = K-total_moves
        if ans%2==0:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
        # if (K-total_moves)%2==0:
        #     print("Yes")
        # else:
        #     print("No")