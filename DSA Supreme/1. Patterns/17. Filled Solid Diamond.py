print("Enter Length of Full Pyramid:")
pyramidLength = int(input())
# print("Enter Total Columns:")
# column = int(input())
for i in range(pyramidLength):
    val = pyramidLength -i
    print("* "*val, end='')
    output_str = ''
    for j in range(i*2):
        output_str += '  '
    # output_str.strip()
    print(output_str,end='')
    print("* "*val, end='')
    # for j in range(pyramidLength-i):
    #     print(' ', end='')
    # print('*'*(pyramidLength-j),end='')
    # for j in range(i):
    #     print('*', end='')
    print("")
    # pass

for i in range(1,pyramidLength+1):
    print("* "*i, end='')
    output_str = ''
    val = pyramidLength -i
    for j in range(val*2):
        output_str += '  '
    # output_str.strip()
    # for j in range(i):
    #     print('*', end='')
    print(output_str,end='')
    print("* "*i, end='')
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