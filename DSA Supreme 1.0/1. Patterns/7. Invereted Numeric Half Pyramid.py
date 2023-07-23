print("Enter Length of Inverted Half Pyramid:")
pyramidLength = int(input())
# print("Enter Total Columns:")
# column = int(input())
for i in range(pyramidLength):
    for j in range(pyramidLength - i):
        print(j+1, end='')
    print("")
    # pass
