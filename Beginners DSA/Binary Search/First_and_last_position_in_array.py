class Solution:
    def first_index(self,nums, target):
        start = 0
        end = len(nums)-1
        mid = start + (end - start)//2
        ans = -1
        while start<=end:
            print(start,end,mid)
            if nums[mid]==target:
                end = mid-1
                ans = mid
            elif target>nums[mid]:
                start = mid+1
            elif target<nums[mid]:
                end = mid-1
            
            mid = start + (end - start)//2
        return ans
    def last_index(self,nums, target):
        start = 0
        end = len(nums)-1
        mid = start + (end - start)//2
        ans = -1
        while start<=end:
            print(start,end,mid)
            if nums[mid]==target:
                start = mid+1
                ans = mid
            elif target>nums[mid]:
                start = mid+1
            elif target<nums[mid]:
                end = mid-1
            mid = start + (end - start)//2
        return ans
    def searchRange(self, nums, target: int):
        # if len(nums)
        return [self.first_index(nums, target),self.last_index(nums, target)]
        
        # print(ans)
        