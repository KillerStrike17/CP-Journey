class Solution:
    def sortedSquares(self, nums):
        output = [f**2 for f in nums]
        output.sort()
        return output
        