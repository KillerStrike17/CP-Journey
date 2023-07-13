def minArray(n, minVal, index, arr):
    if index>=n:
        return minVal
    
    minVal = min(arr[index],minVal)

    return minArray(n,minVal, index+1, arr)

print(minArray(10,10000000,0,[1,2,3,6,7,8,9,-1,6,0]))


def maxValue(n, maxVal, index, arr):
    if index>=n:
        return maxVal
    
    maxVal = max(arr[index],maxVal)

    return maxValue(n,maxVal, index+1, arr)

print(maxValue(10,-10000000,0,[1,2,3,6,7,8,9,-1,6,0]))
