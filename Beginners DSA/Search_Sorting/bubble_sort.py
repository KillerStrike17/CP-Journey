def bubbleSort(arr,n):
    # Write your code here
    # Do not return anything. Update the given array in-place
    
    for i in range(1,n+1):
        swap = False
        for _ in range(n-i):
            if arr[_]>arr[_+1]:
                arr[_],arr[_+1] = arr[_+1],arr[_]
                swap = True
        if swap == False:
            break
            
    pass