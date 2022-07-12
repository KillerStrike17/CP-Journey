def solve(n):
   
    ans = (n-1)*(solve(n-1) + solve(n-2))
    return ans %(10**9 +7)

def solve_memo(n,dp):
    if n==1:
        return 0
    if n==2:
        return 1
    if n in dp:
        return dp[n]
    dp[n] = (((n-1)%(10**9 +7))*((solve_memo(n-1,dp)%(10**9 +7)) + (solve_memo(n-2,dp)%(10**9 +7)))%(10**9 +7))
    return dp[n]

def solve_tab(n):
    dp = {}
    dp[1] =0
    dp[2] = 1
    if n>2:
        for _ in range(3,n+1):
            ans = (_-1)*(dp[_-1] + dp[_-2])
            dp[_] = ans
        return dp[n] %(10**9 +7)         
    else:
        return dp[n]
    
def solve_tab_space(n):
#     dp = {}
    prev_2 =0
    prev_1 = 1
    if n>2:
        for _ in range(3,n+1):
            ans = (_-1)*(prev_1 + prev_2)
            prev_2 = prev_1
            prev_1= ans
        return prev_1 %(10**9 +7)         
    elif n==1:
        return 0
    elif n ==2:
        return 1



def countDerangements(n):
    # Write your code here.
#     dp = {}
#     dp[1] = 0
#     dp[2] = 1
    return solve_tab_space(n)
#     pass



# Main.
t = int(input())
while t:
    n = int(input())
    print(countDerangements(n))
    t = t-1