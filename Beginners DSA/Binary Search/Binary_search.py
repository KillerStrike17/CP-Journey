class Solution:
    
    def search(self, nums, target: int) -> int:
        start = 0
        end = len(nums) -1
        mid = start + (end-start)//2
        ans = -1
        while start<=end:
            if target==nums[mid]:
                ans =  mid
                return ans
            elif target>nums[mid]:
                start = mid +1
            elif target<nums[mid]:
                end = mid - 1
            mid = start + (end-start)//2
        return ans
                
        