my_array = []
def helper(nums,index,my_str):

    if index == len(nums):
        my_array.append(my_str)
    else:
        for _ in list(my_dict[nums[index]]):
            helper(nums,index+1,my_str + _)

    
    
my_dict = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
nums = [2,3,4]
helper(nums, 0,"")
print(my_array)