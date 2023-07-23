print("Input a number")
n = int(input())

print("Printing all digits - Way 1")
for _ in str(n):
    print(_,end = " ")


print("\nPrinting all digits - Way 2")
out = ""
while n>0:
    value = n%10
    out += str(value) + " "
    n = n//10
print(out[::-1].strip())