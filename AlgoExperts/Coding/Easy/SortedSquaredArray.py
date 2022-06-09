def sortedSquaredArray(array):
    # Write your code here.
    y = [x*x for x in array]
    y.sort()
    return y
