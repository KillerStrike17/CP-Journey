print("Enter Length of Inverted Half Pyramid:")
pyramidLength = int(input())

N = 8
for i in range(pyramidLength):
    print('*'*(N-i),end='')
    output = (str(i+1)+'*')*(i+1)
    print(output[:-1],end='')
    print('*'*(N-i))

