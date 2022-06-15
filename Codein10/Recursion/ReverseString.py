def helper(S: str, start: int, end: int) -> str:
    my_string = ""
    if start == end:
        return S[start]
    elif start > end:
        return ""
    else:
        return S[end] + helper(S, start + 1, end-1) + S[start]


def reverse(N: str) -> str:
    return helper(N, 0, len(N)-1)


print(reverse("hi"))
print(reverse("hie"))
