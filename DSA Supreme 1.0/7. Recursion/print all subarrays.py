def print_subarray_util(arr, start, end):

    if end > len(arr):
        return
    
    for _ in range(start, end):
        print(arr[_],end="")
    print("")
    
    print_subarray_util(arr, start, end+1)

def printSubarray(arr):
    for _ in range(len(arr)):
        print_subarray_util(arr,_,_) 


arr = [1,2,3,4,5]
printSubarray(arr)