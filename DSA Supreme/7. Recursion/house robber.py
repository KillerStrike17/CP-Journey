# maxi = -1000000000
class Solution:
    def robHelper(self,nums, index,n,mydict):
        # global maxi
        if index>=n:
            return 0
        if index in mydict.keys():
            return mydict[index]
        val = nums[index]+ self.robHelper(nums, index+2,n,mydict)

        val2 = self.robHelper(nums, index+1,n,mydict)
        mydict[index] = max(val,val2)
        return mydict[index]



    def rob(self, nums: List[int]) -> int:
        # global maxi
        # maxi = -1000000000
        mydict = {}
        return self.robHelper(nums, 0,len(nums),mydict)



