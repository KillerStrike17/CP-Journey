print("Enter Length of Rectangle:")
Length = int(input())
print("Enter breath of Rectangle:")
Breath = int(input())

for i in range(Length):
    for j in range(Breath):
        if (i == 0 or i == Length -1) or (j==0 or j==Breath-1):
            print('*',end ='')
        else:
            print(' ',end ='')
    print("")