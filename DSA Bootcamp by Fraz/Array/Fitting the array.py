class Solution:
    def isFit (self,arr, brr, n) :
        arr.sort()
        brr.sort()
        for _ in range(n):
            if arr[_]>brr[_]:
                return False
        return True