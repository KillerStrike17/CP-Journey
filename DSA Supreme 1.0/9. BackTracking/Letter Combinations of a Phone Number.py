class Solution:

    def solve(self,ans,output, index, digits, mapping):
        if index>=len(digits):
            ans.append(output)
            return
        # print(digits[index])
        val = mapping[digits[index]]
        for i in range(len(val)):
            output +=val[i]
            self.solve(ans,output, index+1, digits, mapping)
            output = output[:-1]
             
        


    
    def letterCombinations(self, digits: str) -> List[str]:
        index = 0
        output = ""
        mapping = {
        '2':"abc",
        '3':"def",
        '4':"ghi",
        '5':"jkl",
        '6':"mno",
        '7':"pqrs",
        '8':"tuv",
        '9':"wxyz"
        }
        ans = []
        if len(digits) ==0:
            return ans
        self.solve(ans,output, index, digits, mapping)
        return ans
