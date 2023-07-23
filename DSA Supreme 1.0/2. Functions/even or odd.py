def evenOrOdd(number:float):
    if number %2==0:
        return "even"
    return "odd"

print("Enter Number:")
num = float(input())
print("Area:",evenOrOdd(num))