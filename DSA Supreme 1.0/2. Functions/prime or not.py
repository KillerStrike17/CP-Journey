def primeOrNot(num:int):
    for _ in range(2,num//2):
        if num%_ ==0:
            print(_)
            return "Not Prime"
    return "Prime"

print("Enter Prime Number")
num = int(input())
print(primeOrNot(num))
        
