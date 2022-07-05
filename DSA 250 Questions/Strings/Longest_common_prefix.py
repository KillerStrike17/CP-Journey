class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # strs,sort()
        min_s = min(strs, key = len)
        for i ,ch in enumerate(min_s):
            for j in strs:
                # print(ch,i,j[:i+1])
                if ch!=j[i:i+1]:
                    return min_s[:i]
        return min_s
                
            