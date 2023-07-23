def factorial(n:int):
    if n==0 or n==1 :
        return 1
    return n * factorial(n-1)

print("Enter number:")
n = int(input())
print("Factorial:",factorial(n))