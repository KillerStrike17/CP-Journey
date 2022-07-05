class Solution:
    my_dict = {}
    def helper(self, nums, index, temp_arr):
        if index ==len(nums):
            if tuple(temp_arr) not in self.my_dict:
                self.my_dict[tuple(temp_arr)] = 1
            return 
        
        temp_arr.append(nums[index])
        self.helper( nums, index+1, temp_arr)
        temp_arr.pop()
        self.helper( nums, index+1, temp_arr)
    
    def subsets(self, nums):
        global my_dict
        self.my_dict = {}
        self.helper(nums, 0,[])
        return self.my_dict.keys()
        