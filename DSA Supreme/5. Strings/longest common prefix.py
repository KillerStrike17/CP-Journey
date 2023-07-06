s = ["codehelp","codenothelp","codwer"]
ans = ""
i = 0
while True:
    curr_ch = 0
    for _ in s:
        if curr_ch ==0:
            curr_ch = _[i]
        elif(_[i] !=curr_ch):
            curr_ch = 0
            break
    if curr_ch ==0:
        break
    ans += curr_ch
    i+=1

print(ans)        
            

