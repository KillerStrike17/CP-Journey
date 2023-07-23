def temperatureConverter(c:float):
    return (c*9)/5 + 32

print("Enter Temperature in celcius")
C = float(input())
print(temperatureConverter(C))