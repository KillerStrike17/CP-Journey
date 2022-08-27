from typing import List

def insertionSort(n: int, arr: List[int]) -> None:
    # Write your code here.\
    for i in range(1,n):
        temp = arr[i]
        counter = i-1
        for j in range(i-1,-1,-1):
            
            if arr[j]>temp:
                arr[j+1] = arr[j]
                counter -=1
            else:
                break
        arr[counter+1] = temp    
        
    pass