print("Enter Length of Full Pyramid:")
pyramidLength = int(input())
# print("Enter Total Columns:")
# column = int(input())
for i in range(pyramidLength):
    for j in range(pyramidLength-i):
        print(' ', end='')
    print('*'*(pyramidLength-j),end='')
    for j in range(i):
        print('*', end='')
    print("")
    # pass
