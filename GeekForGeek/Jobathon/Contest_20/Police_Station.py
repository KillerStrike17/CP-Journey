#User function Template for python3

from typing import List

class Solution:
    
    def solve(self, N : int, a : int , x : List[int]) -> int:
        x.sort()
        return max(abs(a-x[0]) +abs(a-x[1]),abs(a-x[-2]) +abs(a-x[-1]),abs(a-x[0]) +abs(a-x[-1]) )
        
        
        
        
        # code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N,A = [int(i) for i in input().split()]
        
        
        X = [int(i) for i in input().split()]
        
        obj = Solution()
        res = obj.solve(N,A,X)
        
        print(res)
# } Driver Code Ends