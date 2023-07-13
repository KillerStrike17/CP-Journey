
def checksum(n, arr, index, key, key_arrays):
    if index>=n:
        return
    if key == arr[index]:
        key_arrays.append(index)
        # return index
    checksum(n,arr, index+1, key,key_arrays)

key_array = []
checksum(10,[1,2,3,4,6,5,4,3,2,1], 0, 4,key_array)
print(key_array)
