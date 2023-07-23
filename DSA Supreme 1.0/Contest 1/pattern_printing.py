class Solution:
    def printPattern(self, N):
        #code here 
        mystr = ""
        for i in range(1,N+1):
            mystr += '*'*i + " "
        return mystr.strip()
