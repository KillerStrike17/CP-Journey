print("Enter Length of fancy Pyramid:")
pyramidLength = int(input())
val = 1
for i in range(pyramidLength):
    if i+1 ==1:
        print('1')
    elif i+1 ==2:
        print('1 1')
        check = [1,1]
    else:
        output = []
        for j in range(i+1):
            if j ==0 or j == i:
                output.append(1)
            else:
                output.append(check[j-1]+check[j])
        # print(output)
        check  = output
        output = map(str, output)
        print(' '.join(output))


        

        # print(i+1)

