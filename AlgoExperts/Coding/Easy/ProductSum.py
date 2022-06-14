# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.


def productSum(array):
    # Write your code here.

    n = 0
    ans = 0
    for _ in array:
        print(_, ans)
        if type(_) == int:
            ans += _
        else:
            val = 2*array_disolve(_, 2)
            print("value Returned:", val)
            ans += val
    return ans


def array_disolve(array, deg):
    ans = 0
    deg += 1
    for _ in array:
        print(_, ans, deg)
        if type(_) == int:
            ans += _
        else:

            val = deg*array_disolve(_, deg)
            print("value Returned:", val)
            ans += val
    return ans
