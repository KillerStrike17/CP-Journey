class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        count = 0
        count += s.count('IV')*4
        count += s.count('IX')*9
        count += s.count('XL')*40
        count += s.count('XC')*90
        count += s.count('CD')*400
        count += s.count('CM')*900
        s= s.replace('IV','').replace('IX','').replace('XL','').replace('XC','').replace('CD','').replace('CM','')
        for _ in s:
            count += my_dict[_]
        return count
        