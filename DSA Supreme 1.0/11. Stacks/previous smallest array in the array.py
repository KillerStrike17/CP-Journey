

v = [2,1,4,3]
s = [-1]
ans = []
# for i in range(len(s)):
#     output.append(-1)
for i in range(len(v)):
    curr = v[i]
    while s[-1] >=curr and s!=[]:
        s.pop()
    
    ans.append(s[-1])
    s.append(curr)

print(ans)
    
    
