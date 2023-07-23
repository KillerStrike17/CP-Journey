print("Enter Length of fancy Pyramid:")
pyramidLength = int(input())
counter = 1
for i in range(pyramidLength):
    for j in range(i+1):
        print(counter,end =' ')
        counter +=1
    print("")