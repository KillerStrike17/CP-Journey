class Solution:
    def findDuplicate(self, nums) -> int:
        my_dict = {}
        for _ in nums:  
            if _ in my_dict:
                return _
                break
            my_dict[_] = 1
            
        