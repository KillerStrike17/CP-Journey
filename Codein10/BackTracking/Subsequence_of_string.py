my_array = []


def helper(str, index, temp_str):
    if index == len(str):
        if temp_str != "":
            my_array.append(temp_str)
        return
    temp_str += str[index]
    helper(str, index+1, temp_str)
    temp_str = temp_str[:-1]

    helper(str, index+1, temp_str)


def subsequences(str):
    global my_array
    my_array = []
    helper(str, 0, "")

#     print(my_array)
    return my_array
    # Write your code here
    pass
