


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
        

def morePrecision(n,precision, tempSol):
    fac = 1
    ans = tempSol
    for _ in range(precision):
        fac = fac/10
        # print("fac:",fac)
        j=ans
        # print("J:",j)
        while((j*j)<n):
            # print(j,fac)
            ans = j
            j+=fac
            # print(j,fac)
            
    return ans
        


    
    # pass


def sqrtN(n):
    temp =  bs(n)
    return morePrecision(n,3, temp)

	# Write your code here.
# 	pass

print(sqrtN(101))