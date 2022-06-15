# your code goes
my_list = []


def helper(S: list, tempAns: str, index: int):
    if index == len(S):
        # print(tempAns)
        temp = list(filter(None, tempAns.split(' ')))
        temp = sum(list(map(int, temp)))
        my_list.append(temp)
        return
    helper(S, tempAns + ' ' + str(S[index]), index+1)
    helper(S, tempAns, index+1)


def subset(S: str):
    helper(S, " ", 0)


subset([1, 2, 3])
print(my_list)
my_list.sort()
print(my_list)
