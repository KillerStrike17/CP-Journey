my_array = []


def helper(n, k, index, temp_arr):
    if k == len(temp_arr):
        my_array.append(temp_arr.copy())
        return

    if((k-len(temp_arr)) > (len(n)-index+1)):
        return

    if (index == len(n)):
        return

    # if (index == len(n)) or k == len(temp_arr):
    #     my_array.append(temp_arr.copy())
    #     return

    temp_arr.append(n[index])
    helper(n, k, index+1, temp_arr)
    temp_arr.pop()
    helper(n, k, index+1, temp_arr)


def combination(n, k):
    helper(n, k, 0, [])


combination([1, 2, 3, 4], 2)
print(my_array)
