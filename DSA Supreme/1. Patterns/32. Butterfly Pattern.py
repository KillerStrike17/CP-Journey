print("Enter Length of butterfly pattern:")
pyramidLength = int(input())



for i in range(pyramidLength):
    output_str = ''
    output_str+='*'*(i+1)
    # for i in range(pyramidLength):
    output_str+=' '*(pyramidLength-i-1)*2
    # for i in range(pyramidLength):
    output_str+='*'*(i+1)
    print(output_str)

for i in range(pyramidLength,-1,-1):
    output_str = ''
    output_str+='*'*(i)
    # for i in range(pyramidLength):
    output_str+=' '*(pyramidLength-i)*2
    # for i in range(pyramidLength):
    output_str+='*'*(i)
    print(output_str)


# for i in range(pyramidLength,-1,-1):
#     print('*'*(i))