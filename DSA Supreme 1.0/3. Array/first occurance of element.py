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

        start = 0
        end = len(arr) - 1
        mid = start + (end - start)//2
        val = end
        while start<=end:
            if arr[mid] >= x:
                val = mid
                end = mid -1
                # break
            elif arr[mid]<x:
                start +=1
            else:
                end -=1
            mid = start + (end - start)//2
        print(val)
        high = val
        low = val -1
        print(high,low)
        while k>0:
            if low<0:
                high +=1
            elif high>=len(arr):
                low-=1
            elif (x-arr[low])>(arr[high]-x):
                high+=1
            else:
                low-=1
            k-=1

        return arr[low+1:high]