arr = [1,2,3,4]

target = 11

def solve(arr, target):
    mini = 10000000000000
    if target ==0:
        return 0
    if target<0:
        return 100000000000000
    for _ in arr:
        ans = solve(arr, target-_)
        # print(ans)
        mini = min(mini, ans+1)
    return mini 

print((solve(arr, target)))