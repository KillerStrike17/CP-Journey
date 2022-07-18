class Solution:
    def pivotIndex(self, nums) -> int: 
        total = sum(nums)
        left_sum = 0
        for i, v in enumerate(nums):
            print(left_sum, total-left_sum-v)
            if left_sum == (total-v-left_sum):
                return i
            left_sum +=v
        return -1
