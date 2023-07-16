class Solution:

    def isHelperMatching(self,s,si,p,pi):
        print(si,pi)
        if si ==len(s) and pi ==len(p):
            # print("here2")
            return True
        
        if si==len(s) and pi<len(p):
            while pi<len(p):
                if p[pi]!="*":
                    return False
                pi+=1
            return True
        if si<len(s) and pi==len(p):
            return False

        if s[si]==p[pi] or p[pi] =="?":
            # print("Here")
            return self.isHelperMatching(s,si+1,p,pi+1)
        if p[pi]=="*":
            ans = self.isHelperMatching(s,si,p,pi+1)
            ans2 = self.isHelperMatching(s,si+1,p,pi)
            return ans or ans2
        return False


    def isMatch(self, s: str, p: str) -> bool:
        si = 0
        pi = 0
        return self.isHelperMatching(s,si,p,pi)