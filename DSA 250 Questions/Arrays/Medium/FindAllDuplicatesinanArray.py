class Solution:
    def findDuplicates(self, nums):
        my_dict= {}
        output_arr = []
        for _ in nums:
            if _ in my_dict:
                output_arr.append(_)
            else:
                my_dict[_]= 1
        return output_arr
                
                
        