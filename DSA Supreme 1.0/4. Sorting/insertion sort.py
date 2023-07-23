arr = [10,1,7,6,14,9]

print(arr)
n = len(arr)
for i in range(1,n):
    # Fetch
    val = arr[i]
    
    #Compare 
    j = i-1
    swap = False
    while j>=0:
        if arr[j]>val:
            swap = True
            arr[j+1] = arr[j]
        else:
            break
        j-=1
    
    # for j in range(i-1,-1,-1):
    arr[j+1] = val  
    if swap == False:
        break
print(arr)
        
    
    