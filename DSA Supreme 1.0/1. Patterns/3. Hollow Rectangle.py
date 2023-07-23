print("Enter Total Rows:")
row = int(input())
print("Enter Total Columns:")
column = int(input())
for i in range(row):
    for j in range(column):
        if (i==0 or i==(row -1)):
            print('*', end ='')
        elif (j==0 or j==column-1):
            print('*', end ='')
        else:
            print(' ', end ='')       
    print('')