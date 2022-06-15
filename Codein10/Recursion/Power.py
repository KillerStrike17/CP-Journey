# your code goes here
def power(N: int, X: int) -> int:
    """
    N in power value, and X is input variable
    """
    if N == 0:
        return 1
    else:
        return X*power(N-1, X)


print(power(2, 6))
