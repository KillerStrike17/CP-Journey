class Solution:

    def solve(self,ans,n,open,close,output):
        if open == 0 and close ==0:
            ans.append(output)
         
        if open>0:
            output +="("
            self.solve(ans, n,open-1,close,output)
            output = output[:-1]
        if close>open:
            output +=")"
            self.solve(ans, n,open,close-1,output)
            output = output[:-1]



    def generateParenthesis(self, n: int) -> List[str]:
        pass
        open = close = n
        output = ""
        ans = []
        self.solve(ans,n,open,close,output)
        return ans

