class Solution:
    def IsPerfect(self,arr,n):
        check = 0
        for _ in range(n//2):
            # print(arr[_],arr[n-1-_])
            if arr[_] !=arr[n-1-_]:
                # print("here")
                # check = 1
                return False
        return True