class Solution:
    def diagonalSum(self, mat) -> int:
        n = len(mat)
        sum_val = 0
        for _ in range(n):
            sum_val += mat[_][_] + mat[n-1-_][_]
            # print(sum_val)
        if n & 1:
            sum_val -= mat[n//2][n//2]
        return sum_val
