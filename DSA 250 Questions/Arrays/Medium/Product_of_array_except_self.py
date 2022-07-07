class Solution:    
    def productExceptSelf(self, nums):
        output = []
        prefix = [nums[0]]
        
        prod = 1
        for _ in range(1,len(nums)):
            prefix.append(nums[_]*prefix[_-1])
            
        # print(prefix)
        nums2 = nums.copy()[::-1]
        # print(nums2)
        postfix = [nums2[0]]
        for _ in range(1,len(nums)):
            postfix.append(nums2[_]*postfix[_-1])
        postfix = postfix[::-1]
        
        # print(postfix)
        for _ in range(len(nums)):
            
#             if nums[_] ==0:
            if _ ==0:
                output.append(postfix[_+1])
            elif _==len(nums)-1:
                output.append(prefix[_-1])
            else:
                output.append(prefix[_-1]*postfix[_+1])
        
        return output