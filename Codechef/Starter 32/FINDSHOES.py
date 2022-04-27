for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    if M>N:
        print(N)
    else:
        print(2*N-M )

