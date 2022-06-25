def pow(X, N):
    if N == 0:
        return 1
    if N == 1:
        return X
    return X*pow(X, N-1)
    # Write your code here.
    pass
