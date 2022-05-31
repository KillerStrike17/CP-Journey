# cook your dish here
for _ in range(int(input())):
    N = int(input())
    S = input()
    if S.count('1') == 0:
        print(0)
    else:
        val = 1
        for _ in range(N-1):
            if S[_] =='1' and S[_+1]=='1':
                val = 2
                break
        print(val)