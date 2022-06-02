# cook your dish here
for _ in range(int(input())):
    P_A, P_B, Q_A, Q_B = list(map(int, input().split()))
    if max(P_A, P_B) > max(Q_A, Q_B):
        print("Q")
    elif max(Q_A, Q_B) > max(P_A, P_B):
        print("P")
    else:
        print("TIE")
