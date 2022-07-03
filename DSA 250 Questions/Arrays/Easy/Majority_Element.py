from collections import Counter

class Solution:
    def majorityElement(self, nums) -> int:
        dic = Counter(nums)
        max_val = 0
        max_val_2 = 0
        for k in dic:
            # print(k, dic[k],max_val)
            if dic[k]>max_val_2:
                max_val = k
                max_val_2 = dic[k]
        return max_val
        