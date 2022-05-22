# cook your dish here
for _ in range(int(input())):
    S = input()
    S_len = len(S)
    if S_len % 2 == 0:
        A = ''.join(sorted(S[:S_len//2]))
        B = ''.join(sorted(S[S_len//2:]))
        if A == B:
            val = "YES"
        else:
            val = "NO"
    else:
        A = ''.join(sorted(S[:S_len//2]))
        B = ''.join(sorted(S[S_len//2 + 1:]))
        if A == B:
            val = "YES"
        else:
            val = "NO"
        # print(A,B)
    print(val)
