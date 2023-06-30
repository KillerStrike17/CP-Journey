divisor = 22
divident = 7
def bs(divisor, divident):
    ans = -1
    start =0
    end = divident
    mid = start + (end - start)//2
    while start<=end:
        if divident*mid == divisor:
            return mid
        elif divident*mid>divisor:
            end = mid -1
            
        else:
            ans = mid
            start = mid +1
        mid = start + (end - start)//2
    return ans

print(bs(divisor, divident))