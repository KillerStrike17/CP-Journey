def compare(already_visited, current_string):
    self_check = [0]*26
    for _ in current_string:
        if already_visited[ord(_)-97] == 1:
            return False
        if self_check[ord(_)-97] == 1:
            return False
        self_check[ord(_)-97] = 1
    return True


def helper(arr, already_visited, index, temp_str):

    if index == len(arr):
        return len(temp_str)

    current_str = arr[index]
    if compare(already_visited, current_str) == False:
        return helper(arr, already_visited, index+1, temp_str)
    else:
        for _ in current_str:
            already_visited[ord(_)-97] = 1
            temp_str += _
        val = helper(arr, already_visited, index+1, temp_str)
        for _ in current_str:
            already_visited[ord(_)-97] = 0
            temp_str = temp_str[:-1]

        val_2 = helper(arr, already_visited, index+1, temp_str)
        # print(val, val_2)
        return max(val, val_2)


def stringConcatenation(arr):
    already_in_string = [0]*26
    print(helper(arr, already_in_string, 0, ""))

    # Write your code here
    # Return an integer


stringConcatenation(['cha', 'r', 'act', 'ers'])
