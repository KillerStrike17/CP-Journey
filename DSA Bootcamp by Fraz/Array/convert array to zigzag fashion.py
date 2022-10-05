class Solution:
	def zigZag(self,arr, n):
	    for _ in range(n-1):
	        if _%2==0 and arr[_]>arr[_+1]:
	            arr[_],arr[_+1] = arr[_+1],arr[_]

            elif _%2==1 and arr[_]<arr[_+1]:
                arr[_],arr[_+1] = arr[_+1],arr[_]