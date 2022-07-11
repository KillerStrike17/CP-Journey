from collections import Counter
class Solution:
    def firstMissingPositive(self, nums) -> int:
            
        for _ in range(len(nums)):
            if nums[_]<0:
                nums[_] = 0
        
        for _ in range(len(nums)):
            val = abs(nums[_])
            if 1<=val<=len(nums):
                if nums[val-1]>0:
                    nums[val-1] *= -1
                elif nums[val-1]==0:
                    nums[val-1] = (len(nums) + 1)*-1
            
        
        
        for _ in range(1,len(nums)+1):
            if nums[_-1] >=0:
                return _
            
            
        return len(nums) +1 