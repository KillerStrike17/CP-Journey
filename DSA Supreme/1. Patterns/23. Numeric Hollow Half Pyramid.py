print("Enter Length of Inverted Half Pyramid:")
pyramidLength = int(input())

for i in range(pyramidLength):
    for j in range(0,i+1):
        if j == 0 or j ==i or i == pyramidLength-1:
            print(j+1,end ='')
        else:
            print(" ",end ='')
    print("")
