my_array = []


def helper(input, index, temp_arr):
    if index == len(input):
        my_array.append(temp_arr.copy())
        return
    else:
        temp_arr.append(input[index])
        helper(input, index+1, temp_arr)
        temp_arr.pop()

        while ((index < len(input)-1)and(input[index] == input[index+1])):
            index += 1
        helper(input, index+1, temp_arr)


def subset(input):
    index = 0
    temp_arr = []
    helper(input, index, temp_arr)


subset([2, 2, 2])
print(my_array)
