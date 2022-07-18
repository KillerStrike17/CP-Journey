def bs(n):
    target = n
    s = 0
    e = n
    mid = s+(e-s)//2
    ans= 0
    while(s<=e):
        val = mid*mid
        if val==target:
            ans = mid
            return ans
        elif val<target:         
            s = mid +1
            ans = mid
        else:
            e = mid -1
        mid = s+(e-s)//2
    return ans
        
        

def sqrtN(n):
    return bs(n)
	# Write your code here.
# 	pass