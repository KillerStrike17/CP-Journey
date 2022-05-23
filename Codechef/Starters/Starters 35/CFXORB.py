for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    X = int(input())
    for i in range(N):
        A[i] = A[i] & X
    print(A[i])
    ans = 0
    my_dict= {x:A.count(x) for x in A}
    print(my_dict)
    # for _ in A:
    #     ans += A.count(_)*A.count(_)
    # print(ans)
