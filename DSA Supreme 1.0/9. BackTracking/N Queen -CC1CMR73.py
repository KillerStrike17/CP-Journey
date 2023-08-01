
def solve(board, col, n):
    if col>=n:
        printSolution(board,n)
        return
    for row in range(n):
        if isSafe(row,col,board,n):
            board[row][col] = 1
            solve(board, col+1, n)
            board[row][col] = 0