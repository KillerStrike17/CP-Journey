class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        val = - 1
        for _ in range(0, len(nums)-1, 2):
            print(nums[_], nums[_+1])
            if nums[_] != nums[_+1]:
                val = nums[_]
                return val
        if val == -1:
            return nums[-1]
