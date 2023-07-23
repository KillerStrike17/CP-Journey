target = 11
coins = [1,2,5]

def solve(arr, target):
    mini = 100000000
    if target == 0:
        return 0
    if target<0:
        return 100000000
    for _ in arr:

        ans = solve(arr,target-_)
        mini =min(ans+1,mini)
    
    return mini

print(solve(coins, target))