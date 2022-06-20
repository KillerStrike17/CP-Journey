temp_arr = []


def helper(n, k, val, check):
    if val <= 0:
        check = 1
    if val == n and check == 1:
        return temp_arr
    if check == 1:

        val += k
#         print(val)
        temp_arr.append(val)
        helper(n, k, val, check)
    else:
        val -= k
#         print(val)
        temp_arr.append(val)
        helper(n, k, val, check)


def printSeries(n, k):
    # Write your code here
    #     temp_arr = [n]
    global temp_arr
    temp_arr = []
    temp_arr.append(n)
    helper(n, k, n, 0)
    return temp_arr


# printSeries(5, 2)
