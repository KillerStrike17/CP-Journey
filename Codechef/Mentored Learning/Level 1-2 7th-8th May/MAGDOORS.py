# cook your dish here
for _ in range(int(input())):
    S = input()
    M = len(S)
    counter = check = 0

    if S[0] == '1':
        for i in range(1, M):
            if S[i] == '1' and check == 0:
                continue
            elif S[i] == '1' and check == 1:
                counter += 1
                check = 0
            elif S[i] == '0' and check == 1:
                continue
            else:
                counter += 1
                check = 1
    else:
        counter = 1
        for i in range(1, M):
            # print(S[i])
            if S[i] == '0' and check == 0:
                continue
            elif S[i] == '0' and check == 1:
                counter += 1
                check = 0
            elif S[i] == '1' and check == 1:
                continue
            else:
                counter += 1
                check = 1
    print(counter)
