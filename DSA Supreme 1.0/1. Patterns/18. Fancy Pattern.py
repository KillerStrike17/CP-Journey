print("Enter Length of Full Pyramid:")
pyramidLength = int(input())

for i in range(pyramidLength):
    # for j in range(i+1):
        output_str = (str(i+1)+'*')*(1+i)
        print(output_str[:-1])

for i in range(pyramidLength,0,-1):
    # for j in range(i+1):
        output_str = (str(i)+'*')*(i)
        print(output_str[:-1])    