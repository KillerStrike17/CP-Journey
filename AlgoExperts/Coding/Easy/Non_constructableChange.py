def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    x = 0
    for _ in coins:
        print(x, _)
        if _ > x+1:
            return x+1
        x += _

    return x+1
