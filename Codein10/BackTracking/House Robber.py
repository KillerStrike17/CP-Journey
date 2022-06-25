class Solution:

    def helper(self, nums, index, my_dict):
        if index >= len(nums):
            return 0
        if index in my_dict.keys():
            return my_dict[index]

        op1 = nums[index] + self.helper(nums, index+2, my_dict)
        op2 = self.helper(nums, index+1, my_dict)
        my_dict[index] = max(op1, op2)
        return my_dict[index]

    def rob(self, nums) -> int:
        my_dict = {}
        return self.helper(nums, 0, my_dict)


# s = Solution()
# print(s.rob([1, 2, 3, 1]))
