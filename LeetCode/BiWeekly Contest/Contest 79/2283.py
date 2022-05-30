class Solution:
    def digitCount(self, num: str) -> bool:
        N = len(num)
        # print(N)
        val = True
        for _ in range(N):
            # print(_)
            # print(num[_])
            # print(num.count(str(_)))
            if int(num[_]) == num.count(str(_)):
                # val= True
                continue
            else:
                val = False
                break
        return val
