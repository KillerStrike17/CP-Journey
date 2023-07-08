arr = [1,2,3,5,7,8,10,13,14,15,17,20,22,25,30,33,35]

x = 3
n = len(arr)

def bs(arr, start, end, x):
    print(start, end)
    mid = (start + end) //2
    while start<=end:
        if arr[mid] ==x:
            return mid
        elif x>arr[mid]:
            start +=1
        else:
            end -=1
        mid = (start + end) //2
    return -1
    
    
def expSearch(a,n,x):
    if a[0] ==x:
        return 0

    i =1
    while i<n and a[i]<=x:
        # print(arr[i])
        
        i=i*2
    
    return bs(a,i//2,min(i,n-1),x)
    

print(expSearch(arr,n,x))
    