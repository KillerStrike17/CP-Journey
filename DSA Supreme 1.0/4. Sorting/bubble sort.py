arr = [5,4,3,2,1]

print(arr)
for i in range(len(arr)):
    counter = 0
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            counter+=1
    if counter ==0:
        break
print(arr)