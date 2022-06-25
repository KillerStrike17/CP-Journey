my_array = []


def helper(input, n, k, index, temp_arr, temp_sum):
    if temp_sum == n and len(temp_arr) == k:
        # print(temp_arr)
        my_array.append(temp_arr.copy())
        return

    if temp_sum > n:
        return

    if index == len(input):
        return

    temp_sum += input[index]
    temp_arr.append(input[index])
    helper(input, n, k, index+1, temp_arr, temp_sum)
    temp_sum -= input[index]
    temp_arr.pop()

    helper(input, n, k, index+1, temp_arr, temp_sum)


def combintation_sum(n, k):
    helper([1, 2, 3, 4, 5, 6, 7, 8, 9], n, k, 0, [], 0)
    print(my_array)


combintation_sum(9, 3)
