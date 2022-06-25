from collections import Counter


class Solution:
    def isEqual(self, S: str, T: str) -> bool:
        # code here
        S = ''.join(sorted(S))
        T = ''.join(sorted(T))
        # print(S)
        # print(T)
        if S == T:
            return True
        else:
            S_dict = Counter(S)
            T_dict = Counter(T)
            print(S_dict)
            print(T_dict)
            for _ in 


s = Solution()
s.isEqual('vvtscymuokolsbnmgx', 'bbtscymuokolsbnmgx')
