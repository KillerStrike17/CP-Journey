my_array = []


def helper(n, k, index, temp_arr, temp_sum):
    if temp_sum == k and temp_arr not in my_array:
        # print(temp_arr)
        my_array.append(temp_arr.copy())
    elif temp_sum > k:
        return
    if index == len(n):
        return

    temp_arr.append(n[index])
    temp_sum += n[index]

    helper(n, k, index+1, temp_arr, temp_sum)
    temp_arr.pop()
    temp_sum -= n[index]

    while ((index < len(n)-1) and (n[index] == n[index+1])):
        # print("Index", index)
        # print(n[index], n[index+1])
        # print("Temp-arr", temp_arr)
        index += 1
    # print("Temp-arr", temp_arr)
    # print("Index", index)
    helper(n, k, index+1, temp_arr, temp_sum)


def combination_sum(n, k):
    global my_array
    my_array = []
    n.sort()
    # print(n)
    helper(n, k, 0, [], 0)
    return my_array


print(combination_sum([1, 1, 4, 3, 2, 2], 5))
