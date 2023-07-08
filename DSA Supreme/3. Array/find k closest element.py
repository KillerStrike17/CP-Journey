class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        low = 0
        high = len(arr)-1
        # if high ==0:
        #     return arr
        k = k
        x = x
        while high-low>=k:
            if (x - arr[low])>(arr[high]-x):
                low+=1
            else:
                high-=1
        return arr[low:high+1]


