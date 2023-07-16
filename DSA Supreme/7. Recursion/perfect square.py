class Solution:
    def numSquareHelper(self,n):
        if n ==0:
            return 1
        if n<0:
            return 0
        ans = 100000000
        i = 1
        end = sqrt(n)
        while i<=end:
            perfectSquare = i*i
            ways = 1+self.numSquareHelper(n-perfectSquare)
            i+=1
            if ans>ways:
                ans = ways
        return ans

    def numSquares(self, n: int) -> int:
        return self.numSquareHelper(n)-1