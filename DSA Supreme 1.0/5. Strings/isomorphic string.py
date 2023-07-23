s = "abc"
t = "dee"
from collections import defaultdict
mymapping = defaultdict(lambda:0)
val = True
for _ in range(len(s)):
    print(s[_],t[_],mymapping)
    if mymapping[s[_]]!=0 and mymapping[s[_]]==t[_] and mymapping[t[_]]==s[_]:
        print("here")
        pass
    elif mymapping[s[_]]==0 and mymapping[t[_]]==0:
        mymapping[s[_]] = t[_]
        mymapping[t[_]] = s[_]
        print(mymapping)
    else:
        val = False
        break
print(val)
