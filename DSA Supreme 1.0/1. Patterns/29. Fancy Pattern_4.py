print("Enter Length of fancy Pyramid:")
pyramidLength = int(input())
print('*')
for i in range(pyramidLength):
    output_str = ''
    for j in range(i+1):
        # print(i)
        output_str +=str(j+1)
    print('*'+output_str + output_str[:-1][::-1]+'*')

for i in range(pyramidLength-1,0,-1):
    output_str = ''
    for j in range(i):
        # print(i)
        output_str +=str(j+1)
    print('*'+output_str + output_str[:-1][::-1]+'*')
print('*')