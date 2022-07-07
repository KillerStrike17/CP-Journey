import re
class Solution:
    
    def helper(self,start, end, s):
        # print(start, s[start],end, s[end])
        if start>=end:
            return True
        # if start == end:
        #     return True
        if s[start]!=s[end]:
            return False
        return self.helper(start+1, end-1, s)
    
    def isPalindrome(self, s: str) -> bool:
        my_str = "".join(s.split())
        my_str = re.sub('[^A-Za-z0-9]+', '', my_str).lower()
        print(my_str)
        return self.helper(0, len(my_str)-1, my_str)