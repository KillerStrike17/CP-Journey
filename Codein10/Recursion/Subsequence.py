# your code goes
def helper(S: str, tempAns: str, index: int):
    if index == len(S):
        print(tempAns)
        return
    helper(S, tempAns + S[index], index+1)
    helper(S, tempAns, index+1)


def subsequence(S: str):
    helper(S, "", 0)


subsequence("abc")
