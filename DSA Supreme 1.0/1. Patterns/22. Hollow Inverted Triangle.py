print("Enter Length of Inverted Half Pyramid:")
pyramidLength = int(input())
# print("Enter Total Columns:")
# column = int(input())
for i in range(pyramidLength):
    for j in range(pyramidLength-i):
        if i==0 or j ==pyramidLength-i-1 or j ==0:
            print('*', end='')
        else:
            print(" ",end='')
    print("")