def binary_search(arr, size, key):
    start = 0
    end = size -1
    mid = (start +(end-start)//2)
    while(start<=end):
        if key ==arr[mid]:
            return mid
        elif key>arr[mid]:
            start = mid +1
        elif key<arr[mid]:
            end = mid -1
        mid = (start +(end-start)//2)
    return -1
even = [1,3,5,7,9,11]
odd = [2,4,6,8,10]

print(binary_search(even, len(even),11))
print(binary_search(even, len(even),1))
print(binary_search(even, len(even),6))
print(binary_search(odd, len(odd),2))
print(binary_search(odd, len(odd),10))
print(binary_search(odd, len(odd),5))