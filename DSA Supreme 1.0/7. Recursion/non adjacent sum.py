arr = [2,1,4,9]
maxi = -10000000000
def subsum(arr, index, temp_sum,n):
    global maxi
    # print(index)
    if index >= n:
        print("here",temp_sum,maxi)
        maxi  = max(temp_sum,maxi)
        return
    subsum(arr,index+2,temp_sum+arr[index], n)
    # temp_sum+=arr[index]
    subsum(arr,index+1,temp_sum, n)
    # temp_sum-=arr[index] 


subsum(arr, 0, 0,4)
print(maxi)