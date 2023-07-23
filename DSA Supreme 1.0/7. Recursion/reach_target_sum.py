def subsets(index, arr, n,temp_arr,output_arr,temp_sum, target):
   if index>=n:
        if temp_sum == target:
            print(temp_arr)
            output_arr.append(temp_arr.copy())
        return
   else:
      
        subsets(index+1, arr, n,temp_arr,output_arr,temp_sum, target)
        temp_arr.append(arr[index])
        temp_sum+=arr[index]
        subsets(index+1, arr, n,temp_arr,output_arr,temp_sum,target)
        temp_arr.pop()
        temp_sum-=arr[index]

output_arr = []
print(subsets(0,[1,1,1,2,2],5,[],output_arr,0,5))
print(output_arr)
    
