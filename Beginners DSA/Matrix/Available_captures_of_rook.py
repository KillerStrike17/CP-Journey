class Solution:
    def numRookCaptures(self, board) -> int:
        for i, x in enumerate(board):
            if 'R' in x:
                val = i,x.index('R')
        print(val)
        counter = 0
        
        # Up
        index = val[0]-1
        while index>=0:
            if 'B' == board[index][val[1]]:
                break
            elif 'p' == board[index][val[1]]:
                counter+=1
                break
            index -= 1
        
        #down
        index = val[0]+1
        while index<=7:
            if 'B' == board[index][val[1]]:
                break
            elif 'p' == board[index][val[1]]:
                counter+=1
                break
            index += 1
        
        #Left
        index = val[1]-1
        while index>=0:
            if 'B' == board[val[0]][index]:
                break
            elif 'p' == board[val[0]][index]:
                counter+=1
                break
            index -= 1
        
        
        index = val[1]+1
        while index<=7:
            if 'B' == board[val[0]][index]:
                break
            elif 'p' == board[val[0]][index]:
                counter+=1
                break
            index += 1
        return counter    
        # bishop = []
        # pawns = []
        # for _ in range(8):
        #     if 'B' in board[val[0]][_]
            
            
        