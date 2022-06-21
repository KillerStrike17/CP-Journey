my_array = []


def helper(s, index, temp_str, my_dict):
    if index == len(s):
        #         print(temp_str)
        my_array.append(temp_str)
        return
    temp = my_dict[int(s[index])]
#     print()
    for _ in list(temp):
        temp_str += _
        helper(s, index+1, temp_str, my_dict)
        temp_str = temp_str[:-1]

#     helper(s, index, temp_str):


def combinations(s):
    global my_array
    my_array = []
    my_dict = {2: "abc", 3: "def", 4: "ghi", 5: "jkl",
               6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
#     print(my_array)
    helper(s, 0, "", my_dict)
    return my_array
    # Write your code here
    pass


combinations("23")
