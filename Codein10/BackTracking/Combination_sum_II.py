my_array = []


def helper(n, target, index, temp_arr, temp_sum):
    #     print(temp_sum, temp_arr)
    if temp_sum == target:
        my_array.append(temp_arr.copy())
        return
    if index == len(n):
        return
    if temp_sum > target:
        return
    temp_arr.append(n[index])
    temp_sum += n[index]
    helper(n, target, index, temp_arr, temp_sum)
    temp_arr.pop()
    temp_sum -= n[index]

    helper(n, target, index+1, temp_arr, temp_sum)


def combSum(ARR, B):

        # Write your code here
        # Return a list of sorted lists/combinations
    global my_array
    my_array = []
    helper(ARR, B, 0, [], 0)
#     print(my_array)
    my_array = list(map(sorted, my_array))
    # print(temp)
    # my_array = [sorted(x, key=lambda x: x[0]) for x in my_array]
    return my_array


print(combSum([3, 2, 1], 5))
