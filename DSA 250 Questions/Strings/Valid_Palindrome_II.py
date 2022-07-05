import itertools
class Solution:    
    def validPalindrome(self, s: str) -> bool:
        x = len(s)
        start = 0
        end = x-1
        s = list(s)
        for _ in range(x):
            if s[start]!=s[end]:
                temp=s.copy()
                val = temp[start]
                temp.pop(start)
                if temp ==temp[::-1]:
                    return True
                temp.insert(start, val)
                temp.pop(end)
                if temp ==temp[::-1]:
                    return True
                else:
                    return False
            start +=1
            end -=1
        return True