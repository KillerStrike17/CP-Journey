my_list = []


def helper(S, i):
    # print(S, i)
    # print(len(S))
    if i == len(S):
        my_list.append(S.copy())
        return
    for _ in range(i, len(S)):
        # print("Before:", S)
        S[i], S[_] = S[_], S[i]
        # print("After:", S)
        helper(S, i+1)
        S[i], S[_] = S[_], S[i]
    # sys.exit(0)
    return


helper([1, 2, 3], 0)
print(my_list)


#v2

class Solution:
    my_arr = []
    def helper(self, nums:List[int],index):
        if index==len(nums):
            self.my_arr.append(nums.copy())
        
        for _ in range(index, len(nums)):
            nums[_],nums[index] = nums[index],nums[_]
            self.helper(nums,index+1)
            nums[_],nums[index] = nums[index],nums[_]
        
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.my_arr = []
        self.helper(nums, 0)
        return self.my_arr
        
        