print("Enter Length of Inverted Half Pyramid:")
pyramidLength = int(input())

for i in range(pyramidLength):
    print(i+1,end='')
    for j in range(i+1,pyramidLength):
        if j ==pyramidLength-1 or i ==0:
            print(j+1,end ='')
        else:
            print(" ",end='')
    print("")
