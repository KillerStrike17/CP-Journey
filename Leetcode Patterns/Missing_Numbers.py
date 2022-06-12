class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for _ in range(n):
            if _ != nums[_]:
                return _
        return n
