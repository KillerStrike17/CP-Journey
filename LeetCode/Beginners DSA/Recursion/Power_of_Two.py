def helper(current_val, n):
    #     print(current_val, n)
    if current_val > n:
        return False
    elif current_val == n:
        return True
    return helper(current_val*2, n)


def isPowerOfTwo(n):
    # Write your code here
    if n < 0:
        return False
    else:
        return helper(1, n)
    pass
