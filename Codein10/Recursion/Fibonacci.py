# your code goes here
def FibonacciSeries(N):
    if N == 0:
        return 0
    if N == 1 or N == 2:
        return 1
    else:
        return FibonacciSeries(N-1) + FibonacciSeries(N-2)

print(FibonacciSeries(6))
