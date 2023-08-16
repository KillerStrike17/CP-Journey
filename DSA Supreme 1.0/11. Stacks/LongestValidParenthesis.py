def longestValidParenthesis(s):
    myarr = []
    myarr.append(-1)
    maxLen = 0
    for _ in range(len(s)):
        if s[_] =='(':
            myarr.append(_)
        else:
            myarr.pop()
            if myarr == []:
                myarr.append(_)
            else:
                maxLen = max(maxLen,_-myarr[-1])
    return maxLen

print(longestValidParenthesis(")()())()"))
    
