my_array = []
def helper(array, index, temp_arr ):
    if index ==len(array):
        my_array.append(temp_arr.copy())
        return 

    temp_arr.append(array[index])
    helper(array, index+1, temp_arr)
    temp_arr.pop()
    helper(array, index+1, temp_arr)

def powerset(array):
    # Write your code here.
    global my_array
    my_array = []
    helper(array, 0,[] )
    return my_array
    pass
