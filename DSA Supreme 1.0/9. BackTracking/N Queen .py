def isSafe(row,col,board,n):
    i = row
    j = col
    while j>=0:
        if board[i][j]=='Q':
            return False
        j-=1
    
    i = row
    j = col
    while(i>=0 and j>=0):
        if board[i][j] =='Q':
            return False
        i-=1
        j-=1
    
    i = row
    j = col
    while(i<n and j>=0):
        if board[i][j] =='Q':
            return False
        i+=1
        j-=1
    return True


def printSolution(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end = "")
        print(" ")
    print("")

def solve(board, col, n):
    if col>=n:
        printSolution(board,n)
        return
    for row in range(n):
        if isSafe(row,col,board,n):
            board[row][col] = 'Q'
            solve(board, col+1, n)
            board[row][col] = '-'


# row = 4
# col = 4
n = col = row = 9
board = []
for i in range(row):
    temp = []
    for j in range(col):
        temp.append('-')
    board.append(temp)
print(board)
solve(board, 0, n)
