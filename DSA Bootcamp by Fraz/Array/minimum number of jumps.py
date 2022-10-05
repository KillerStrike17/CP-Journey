class Solution:
	def minJumps(self, arr, n):
	    if n<2:
	        return 0
	    if arr[0]==0:
	        return -1
        
        maxReach = arr[0]
        step = arr[0]
        res = 1
        
        	        
	    for _ in range(1,n):
	        if _ ==n-1:
	            return res
	        maxReach = max(maxReach, _+arr[_])
	       # print("maxReach:",maxReach)
	        step -= 1
	        if step==0:
	            res +=1
	            if _>=maxReach:
	                return -1
	           
	            
	            step = maxReach-_
	    return -1