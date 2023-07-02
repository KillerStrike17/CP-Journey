# all elements occur even number of time
# all repeating occurance of elments appears
# in pairs and all pairs are not adjecent,
# there cannot be more than 2 consecutive lement

# find the elements that appears odd number of times

x = [1,1,2,2,3,3,4,4,3,600,600,4,4]

# ans = 0
# for _ in x:
#     ans ^=_

# print(ans)

def bs(x):
    s = 0
    e = len(x)-1
    m = s+(e-s)//2
    while s<=e:
        # print(m)
        if (s==e):
            return s
        # if (m%2==0):
        if(m&1==0):
            if x[m]==x[m+1]:
                s = m+2
            else:
                e = m                
        else:
            if x[m]==x[m-1]:
                s = m+1
            else:
                e = m-1
        m = s+(e-s)//2
    return -1
    
print(bs(x))