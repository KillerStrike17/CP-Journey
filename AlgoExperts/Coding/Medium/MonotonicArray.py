def isMonotonic(array):
    # Write your code here
    x = array.copy()
    y = array.copy()
    x.sort()
    y.sort(reverse=True)
    if x == array or y == array:
        return True
    else:
        return False
    # pass
