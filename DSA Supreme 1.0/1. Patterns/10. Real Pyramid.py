print("Enter Length of Full Pyramid:")
pyramidLength = int(input())
# print("Enter Total Columns:")
# column = int(input())
for i in range(pyramidLength):
    val = pyramidLength -i
    print(" "*val, end='')
    output_str = ''
    for j in range(i+1):
        output_str += '* '
    output_str.strip()
    print(output_str,end='')
    print(" "*val, end='')
    # for j in range(pyramidLength-i):
    #     print(' ', end='')
    # print('*'*(pyramidLength-j),end='')
    # for j in range(i):
    #     print('*', end='')
    print("")
    # pass
