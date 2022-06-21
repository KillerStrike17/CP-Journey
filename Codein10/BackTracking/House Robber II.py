class Solution:
    def helper(self, nums, index, temp_sum):
        # print(index)
        if index > len(nums):
            return
        elif len(nums) > 2:
            if len(nums) % 2 != 0:
                temp_sum += nums[0]
                self.helper(nums[:-1], index+2, temp_sum)
                # temp_sum -= nums[0]
                val = temp_sum
                temp_sum = 0
                temp_sum += nums[-1]
                self.helper(nums[1:][::-1], index+2, temp_sum)
                val = max(val, temp_sum)

                temp_sum = 0
                temp_sum += nums[1]
                index = 1
                self.helper(nums[1:], index+2, temp_sum)
                # temp_sum -= nums[1]
                val = max(val, temp_sum)
                # print(val, val_2, val_3)
                return val
            else:
                temp_sum += nums[0]
                self.helper(nums, index+2, temp_sum)
                # temp_sum -= nums[0]
                val = temp_sum
                # print(temp_sum)
                # sys.exit(0)
                temp_sum = 0
                temp_sum += nums[1]
                index = 1
                val_2 = self.helper(nums, index+2, temp_sum)
                # temp_sum -= nums[1]
                return max(val, temp_sum)

    def rob(self, nums: list) -> int:
        return self.helper(nums, 0, 0)


s = Solution()
print(s.rob([1, 2, 3, 1]))
