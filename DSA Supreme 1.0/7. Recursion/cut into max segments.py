N = 10
x = 5
y = 2
z = 2

def solve(N, x,y,z):
    if N ==0:
        return 0
    if N<=0:
        return -1000000000
    
    a = solve(N-x,x,y,z) +1

    b = solve(N-y,x,y,z) +1
    
    c = solve(N-z,x,y,z) +1
    
    return max(a,b,c)

val = solve(N, x,y,z)
if val<0:
    print(0)
else:
    print(val)
