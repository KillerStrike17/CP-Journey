''' 
    Time Complexity : O(N)
    Space Complexity : O(N)
    
    Where ‘N’ is the number of stairs.
'''

from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)


MOD = 1000000007


def countDistinctWayToClimbStair(nStairs):

    dp = [-1 for i in range(nStairs+1)]

    #   For single stair only
    dp[0] = 1

    #   For two stairs
    dp[1] = 1

    #   Go all stairs
    for currStep in range(2, nStairs+1):
        #   Get the number of way to reach currStep
        dp[currStep] = (dp[currStep - 1] + dp[currStep - 2]) % MOD

    return dp[nStairs]


#   taking inpit using fast I/O
def takeInput():
    n = int(stdin.readline().strip())
    return n


#   main
T = int(input())
while (T > 0):
    T -= 1
    n = takeInput()
    ans = countDistinctWayToClimbStair(n)
    print(ans)
