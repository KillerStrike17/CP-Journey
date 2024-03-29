class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        x = len(nums)
        running = []
        for _ in range(x):
            if _ != 0:
                running.append(nums[_] + running[_-1])
            else:
                running.append(nums[_])
        return running
