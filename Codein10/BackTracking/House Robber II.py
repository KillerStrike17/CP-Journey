class Solution:
    def helper(self, nums, index, my_dict):
        if index >= len(nums):
            return 0
        if index in my_dict.keys():
            return my_dict[index]

        op1 = nums[index] + self.helper(nums, index+2, my_dict)
        op2 = self.helper(nums, index+1, my_dict)
        my_dict[index] = max(op1, op2)
        print(my_dict)
        return my_dict[index]

    def rob(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        my_dict = {}
        x = self.helper(nums[1:], 0, my_dict)
        # print(x)
        my_dict = {}
        y = self.helper(nums[:-1], 0, my_dict)
        # print(y)
        return max(x, y)
