# cook your dish here
T = int(input())


def score_consistent(T):
    for _ in range(T):
        A, B = [int(x) for x in input().split()]
        C, D = [int(x) for x in input().split()]
        # print(A,C)
        # print(B,D)
        if C >= A and D >= B:
            print("POSSIBLE")
        else:

            print("IMPOSSIBLE")


score_consistent(T)
