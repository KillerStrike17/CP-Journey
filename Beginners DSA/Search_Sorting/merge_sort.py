def merge(arr, s,e):
    mid = s+(e-s)//2
    len1 = mid-s+1
    len2 = e-mid
    first = arr[s:len1+1].copy()
    second = arr[len2:e+1].copy()
    index1=0
    index2=0
    mainArrayIndex = s
    print(len1,len2)
    print(first, second)
    while(index1<len1 and index2<len2):
        print(index1,index2)
        if first[index1]<second[index2]:
            arr[mainArrayIndex] = first[index1]
#             mainArrayIndex +=1
            index1+=1
        else:
            
            arr[mainArrayIndex] = second[index2]
            index2+=1
        mainArrayIndex+=1
    
    while(index1<len1):
        arr[mainArrayIndex] = first[index1]
        index1+=1
        mainArrayIndex+=1
    while(index2<len2):
        arr[mainArrayIndex] = second[index2]
        index2+=1
        mainArrayIndex+=1        
        
        
    
def Msort(arr, s,e):
    if s>=e:
        return 
    print('HI')
    mid = s+(e-s)//2
    print(s,e,mid)
    Msort(arr, s, mid)
    Msort(arr, mid+1,e)
    merge(arr, s, e)

def mergeSort(arr, n):
    Msort(arr, 0,n-1)
    # Write your code here.
    pass

mergeSort([1,3,4,6,2],5)