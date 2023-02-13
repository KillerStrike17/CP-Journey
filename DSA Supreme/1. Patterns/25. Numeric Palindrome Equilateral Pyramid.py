print("Enter Length of Inverted Half Pyramid:")
pyramidLength = int(input())

for i in range(pyramidLength):
    output_str = ' '*(pyramidLength-i-1)
    for j in range(i+1):
        # output_str+=
        output_str +=str(j+1)
    print(output_str+output_str[:-1][::-1],end='')
    print("")
    # break