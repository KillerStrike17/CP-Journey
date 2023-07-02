arr = [5,4,3,2,1]

print(arr)
for i in range(len(arr)-1):
    minVal = i
    
    for j in range(i+1, len(arr)):
        if arr[j]<arr[minVal]:
            minVal = j
    arr[i], arr[minVal] =  arr[minVal],arr[i]
    print(f"pass {i+1}:", arr)

print(arr)
        
    