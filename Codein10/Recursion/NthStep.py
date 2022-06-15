# your code goes here
def nthStep(N: int) -> int:
    if N == 1:
        return 1
    if N == 2:
        return 2
    else:
        return nthStep(N-1) + nthStep(N-2)


print(nthStep(6))
