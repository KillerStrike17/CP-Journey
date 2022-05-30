def twoNumberSum(array, targetSum):
    # Write your code here.
    # # valuedict = {}
    array.sort()
    my_array = []
    if len(array) > 1:
        for _ in array:
            val = targetSum - _
            if val in array:
                my_array.append(val)
                my_array.append(_)
                break
    return my_array
