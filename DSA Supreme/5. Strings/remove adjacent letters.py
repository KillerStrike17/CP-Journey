mystr = "azxxzy"
ans = []
for _ in list(mystr):
    if  ans and _ ==ans[-1]:
        ans.pop()
    else:
        ans.append(_)
print("".join(ans))
