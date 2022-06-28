def firstDuplicateValue(array):
    my_dict = {}
    for _ in array:
        if _ in my_dict:
            return _
        else:
            my_dict[_] = 1
        
    # Write your code here.
    return -1
