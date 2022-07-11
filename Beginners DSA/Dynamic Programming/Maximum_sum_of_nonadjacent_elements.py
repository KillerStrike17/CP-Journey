from sys import stdin

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    n = len(nums)
#     ans = helper(n-1, nums,dp)
#     return ans
    i_1 = nums[0]
    i_2 = 0
    ans = nums[0]
    for _ in range(1,n):
        inc = i_2 + nums[_]
        exc = i_1+0
        ans = max(inc,exc)
        i_2 = i_1
        i_1 = ans
    return ans
# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1