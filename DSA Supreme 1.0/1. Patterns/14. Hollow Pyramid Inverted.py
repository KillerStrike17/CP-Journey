print("Enter Length of Full Pyramid:")
pyramidLength = int(input())
# print("Enter Total Columns:")
# column = int(input())
for i in range(pyramidLength):
    output_str = ''
    for j in range(pyramidLength-i):
        if j ==0 or j == pyramidLength-i-1:
            output_str += '* '
        else:
            output_str += '  '
    output_str.strip()
    for j in range(i):
        print(' ', end='')
    print(output_str,end='')
    # val = i
    # print(" "*val, end='')
    # 
    
    # print(" "*val, end='')
    # for j in range(pyramidLength-i):
    #     print(' ', end='')
    # print('*'*(pyramidLength-j),end='')
    # for j in range(i):
    #     print('*', end='')
    print("")
    # pass
