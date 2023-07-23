def partition(arr,s,e):
    pivotIndex = s
    pivotElement = arr[s]
    i = s-1
    for j in range(s, e):
        if arr[j] > pivotElement:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (arr[i], arr[j]) = (arr[j], arr[i])
    # Swap the pivot element with the greater element specified by i
    (arr[i + 1], arr[e]) = (arr[e], arr[i + 1])
    return i+1
 
    

def quicksort(arr,s, e):
    if s>=e:
        return
    # Partition Logic
    index = partition(arr, s, e)
    
    quicksort(arr,s,index-1)
    quicksort(arr,index+1,e)


arr = [7,3,2,11,2,2,2,2,16,24,4,11,9]
print(arr)
quicksort(arr,0,len(arr)-1)
print(arr)