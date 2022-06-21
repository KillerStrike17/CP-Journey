my_arr = []


def helper(arr, n, k, index, temp_sum, temp_arr):
    # if temp_sum > k:
    #     return
    #     if len(temp_arr) > 0 and temp_sum == k:
    # #         print(temp_arr)
    #         my_arr.append(temp_arr.copy())
    #         return
    if index == n:
        if temp_sum == k and len(temp_arr) > 0:
            my_arr.append(temp_arr.copy())
        return

    temp_sum += arr[index]
    temp_arr.append(arr[index])
    helper(arr, n, k, index+1, temp_sum, temp_arr)
    temp_sum -= arr[index]
    temp_arr.pop()

    helper(arr, n, k, index+1, temp_sum, temp_arr)


def findSubsetsThatSumToK(arr, n, k):
    # Write your code here.
    global my_arr
    my_arr = []
#     arr.sort()
    helper(arr, n, k, 0, 0, [])
    return my_arr


#     pas
print(findSubsetsThatSumToK(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 16, 0))
