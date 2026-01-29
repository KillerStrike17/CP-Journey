def decimal_to_binary(n):
    output_str = ""
    while n>0:
        b = n%2
        print(b)
        output_str = str(b)+output_str
        n = n//2
    return output_str

def decimal_to_binary_division_method (n):
    output_str = ""
    while n>0:
        b = n%2
        print(b)
        output_str = str(b)+output_str
        n = n//2
    return output_str

def binary_to_decimal(n):
    length_n = len(n)-1
    output_decimal = 0
    for index,bit in enumerate(n):
        print(index,bit)
        output_decimal += int(bit)*pow(2,length_n-index)
    return output_decimal
value = 100 
x = decimal_to_binary(value)
print(x)
print(binary_to_decimal(x))