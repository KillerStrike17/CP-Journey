my_array = []


def isSafe(i, j, board, n):

    # Up
    tempI = i
    while tempI >= 0:
        if board[tempI][j] == 1:
            return False
        tempI -= 1

    # Top Right
    tempI = i
    tempJ = j
    while tempI >= 0 and tempJ <= n-1:
        if board[tempI][tempJ] == 1:
            return False
        tempI -= 1
        tempJ += 1
    # Top Left
    tempI = i
    tempJ = j
    while tempI >= 0 and tempJ >= 0:
        if board[tempI][tempJ] == 1:
            return False
        tempI -= 1
        tempJ -= 1

    return True


def place(n, board, i):
    #     print(i)
    if i == n:
        #         print("Here")
        val = [x for xs in board for x in xs]
#         print(val)
        my_array.append(val.copy())
        return
    for j in range(n):
        x = isSafe(i, j, board, n)
        # print(x)
        if x == True:
            board[i][j] = 1
            place(n, board, i+1)
            board[i][j] = 0

            # place(n, board, i+1)


def solveNQueens(n):
    # Write your code here.
    global my_array
    my_array = []
    board = []
    for _ in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        board.append(temp)

#     print(board)
    place(n, board, 0)
    return my_array
#     print(my_array)
    pass


solveNQueens(4)
