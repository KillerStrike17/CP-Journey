print("Enter Length of Inverted Half Pyramid:")
pyramidLength = int(input())

for i in range(pyramidLength):
    print('*'*(i+1))

for i in range(pyramidLength-2,-1,-1):
    print('*'*(i+1))