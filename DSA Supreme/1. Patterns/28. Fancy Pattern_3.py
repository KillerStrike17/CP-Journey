print("Enter Length of fancy Pyramid:")
pyramidLength = int(input())
counter = 1
for i in range(pyramidLength):
    output_str = ''
    for j in range(i+1):
        output_str += str(counter) + '*'
        counter +=1
    print(output_str[:-1])
counter -=1
for i in range(pyramidLength,0,-1):
    output_str = ''
    # counter = counter -i +1
    for j in range(i):
        output_str = str(counter) + '*' + output_str
        counter-=1
    print(output_str[:-1])

