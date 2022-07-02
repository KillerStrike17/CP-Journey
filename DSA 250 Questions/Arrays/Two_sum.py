class Solution:
    def twoSum(self, nums, target: int):
        arr = []
        x = len(nums)
        for _ in range(x):
            # print(_,x-1)
            if _ !=x-1:
                # print('here')
                val = target-nums[_]
                # print(val)
                if val in nums[_+1:]:
                    # print('here')
                    arr.append(_)
                    if target-nums[_] == nums[_]:
                        print("here")
                        arr.append(_+1+nums[_+1:].index(target-nums[_]))
                    else:
                        arr.append(nums.index(target-nums[_]))
                    break
        return arr
            