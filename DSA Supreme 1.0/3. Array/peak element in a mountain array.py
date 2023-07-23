a = [0,10,11,12,13,14,15,5,2]

start = 0
end = len(a)-1
mid = (start+end)//2

while start<end:
    if a[mid]>a[mid-1] and a[mid]>a[mid+1]:
        print(a[mid])
        break
    elif a[mid]>a[mid-1]:
        start = mid + 1
    elif a[mid]>a[mid+1]:
        end = mid -1
    
    mid = (start+end)//2
        
    