
def checksum(n, arr, index, key):
    if index>=n:
        return -1
    if key == arr[index]:
        return index
    return checksum(n,arr, index+1, key)

print(checksum(10,[1,2,3,4,6,5,4,3,2,1], 0, 4))