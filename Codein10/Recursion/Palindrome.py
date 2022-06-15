# your code goes here
def helper(S: str, start: int, end: int):
    if start >= end:
        return 1
    if S[start] != S[end]:
        return 0
    return helper(S, start+1, end-1)


def Palindrome(N: str) -> bool:
    return helper(N, 0, len(N)-1)


print(Palindrome("olalo"))
