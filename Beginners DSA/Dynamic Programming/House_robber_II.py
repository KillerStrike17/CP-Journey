def solve(valueInHouse):
    prev_2 = 0
    prev_1 = valueInHouse[0]
    ans = prev_1
    for _ in range(1,len(valueInHouse)):
        inc =prev_2+ valueInHouse[_]
        exc = prev_1
        ans =max(inc,exc)
        prev_2 = prev_1
        prev_1 = ans
    return prev_1

def houseRobber(valueInHouse):
    if len(valueInHouse) ==1:
        return valueInHouse[0]
    return max(solve(valueInHouse[1:]),solve(valueInHouse[:-1]))
    
    
    
    pass