def solve(n,x,y,z):
    if n<0:
        return -1e9
    
    if n==0:
        return 0
    a = solve(n-x,x,y,z) + 1
    b = solve(n-y,x,y,z) + 1
    c = solve(n-z,x,y,z) + 1
    
    ans = max(a,b,c)
    return ans

def solve_memo(n,x,y,z,dp):
    if n<0:
        return -1e9
    if n in dp:
        return dp[n]
    if n==0:
        return 0
    a = solve_memo(n-x,x,y,z,dp) + 1
    b = solve_memo(n-y,x,y,z,dp) + 1
    c = solve_memo(n-z,x,y,z,dp) + 1
    
    dp[n] = max(a,b,c)
    return dp[n]
    
def solve_tab(n,x,y,z):
    
    dp  = [-1e9]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        if (i-x)>=0:
            dp[i]= max(dp[i],dp[i-x]+1)
        if (i-y)>=0:
            dp[i]= max(dp[i],dp[i-y]+1)
        if (i-z)>=0:
            dp[i]= max(dp[i],dp[i-z]+1)
    
    return dp[n]
    
    
    

def cutSegments(n, x, y, z):
    # Write your code here.
    ans = solve_tab(n,x,y,z)
    if ans <0:
        return 0
    return ans
    pass