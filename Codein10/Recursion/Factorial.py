# your code goes here
def factorial(N):
    if N == 1 or N == 0:
        return 1
    else:
        return N*factorial(N-1)


print(factorial(1))
