# cook your dish here
import string
special_chars = string.punctuation

for _ in range(int(input())):
    S = input()
    N = len(S)
    up = low = dig = spc = 0
    if N >= 10:
        for _ in range(N):
            if S[_].isupper() and _ != 0 and _ != N-1:
                up = 1
            if S[_].islower():
                low = 1
            if S[_].isdigit() and _ != 0 and _ != N-1:
                dig = 1
            if S[_] in special_chars and _ != 0 and _ != N-1:
                spc = 1
        if up == 1 and low == 1 and dig == 1 and spc == 1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
