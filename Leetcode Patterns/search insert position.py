class Solution:
    def bs(self,nums, target ):
        start = 0
        end = len(nums)-1
        mid = (start+end)//2
        index = -1
        while end>=start:
            print(start,end,mid)
            if nums[mid]==target:
                index = mid
                start = mid+1
            elif nums[mid]<target:
                start = mid +1
            else:
                end = mid -1

            mid = (start+end)//2
        if index !=-1:
            return index
        else:
            return mid+1

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.bs(nums, target )