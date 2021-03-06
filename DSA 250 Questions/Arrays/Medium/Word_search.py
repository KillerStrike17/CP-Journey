class Solution:
    def search(self,i,j,n,m,board,word,k):
        if k ==len(word):
            return True
        if i<0 or j<0 or i==n or j==m or board[i][j] !=word[k]:
            return False
        val = board[i][j]
        board[i][j] = '#'
        op1 = self.search(i+1,j,n,m,board,word,k+1)
        op2 = self.search(i,j+1,n,m,board,word,k+1)
        op3 = self.search(i-1,j,n,m,board,word,k+1)
        op4 = self.search(i,j-1,n,m,board,word,k+1)
        board[i][j] = val
        return op1 or op2 or op3 or op4
    
    def exist(self, board, word: str) -> bool:
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] ==word[0]:
                    if self.search(i,j,n,m,board,word,0):
                        return True
        return False
        