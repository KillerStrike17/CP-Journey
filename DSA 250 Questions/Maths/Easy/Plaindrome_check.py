class Solution:
    def isPalindrome(self, x: int) -> bool:
        if int(x)>=0:
            if str(x) ==str(x)[::-1]:
                return "true"
            else:
                return "false"
        else:
            return "false"