class Solution:
    def helper(self, nums, temp_sum, index):

        if index >= len(nums):
            # print(temp_sum)
            return temp_sum

        temp_sum += nums[index]
        val = self.helper(nums, temp_sum, index + 2)
        # temp_sum -= nums[index]

        return val

    def rob(self, nums) -> int:
        val = self.helper(nums, 0, 0)
        val2 = self.helper(nums[1:], 0, 0)
        print(val, val2)
        return max(val, val2)


s = Solution()
print(s.rob([1, 2, 3, 1]))
