my_list = []


def helper(S, i):
    # print(S, i)
    # print(len(S))
    if i == len(S):
        my_list.append(S.copy())
        return
    for _ in range(i, len(S)):
        # print("Before:", S)
        S[i], S[_] = S[_], S[i]
        # print("After:", S)
        helper(S, i+1)
        S[i], S[_] = S[_], S[i]
    # sys.exit(0)
    return


helper([1, 2, 3], 0)
print(my_list)
